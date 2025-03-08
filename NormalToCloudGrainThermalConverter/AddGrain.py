import cv2
import numpy as np
import os


def add_film_grain(image_path, intensity=0.7, color_shift=True, save_output=True):
    try:
        image = cv2.imread("Inputs/" + image_path)
        if image is None:
            raise Exception(f"Görüntü yüklenemedi: {image_path}")
    except Exception as e:
        print(f"Hata: {e}")
        return None

    # Görüntünün boyutlarını al
    height, width, channels = image.shape

    # Yüksek yoğunluklu RGB gürültü oluştur
    noise = np.zeros_like(image, dtype=np.float32)

    # Her kanal için farklı gürültü parametreleri kullan
    noise[:, :, 0] = cv2.randn(np.zeros((height, width), dtype=np.float32), 0, 80 * intensity)  # B kanalı
    noise[:, :, 1] = cv2.randn(np.zeros((height, width), dtype=np.float32), 0, 70 * intensity)  # G kanalı
    noise[:, :, 2] = cv2.randn(np.zeros((height, width), dtype=np.float32), 0, 90 * intensity)  # R kanalı

    # Gürültüyü görüntüye ekle
    grainy_image = cv2.add(image.astype(np.float32), noise)

    # İsteğe bağlı renk kayması
    if color_shift:
        # Renk kanallarını hafifçe kaydır
        grainy_image[:, :, 0] = np.clip(grainy_image[:, :, 0] * 1.05, 0, 255)  # Mavi kanalını artır
        grainy_image[:, :, 1] = np.clip(grainy_image[:, :, 1] * 0.95, 0, 255)  # Yeşil kanalını azalt
        grainy_image[:, :, 2] = np.clip(grainy_image[:, :, 2] * 1.03, 0, 255)  # Kırmızı kanalını artır

    # Contrast ayarlaması
    alpha = 1.15  # Contrast değeri (1.0'dan büyükse contrast artar)
    beta = -5  # Parlaklık değeri (negatif değerler karanlığı artırır)
    grainy_image = cv2.convertScaleAbs(grainy_image, alpha=alpha, beta=beta)

    # Değerleri geçerli aralığa getir
    grainy_image = np.clip(grainy_image, 0, 255).astype(np.uint8)

    # Hafif bir bulanıklaştırma uygula (grain'in daha doğal görünmesi için)
    grainy_image = cv2.GaussianBlur(grainy_image, (3, 3), 0.5)

    # Tekrar grain ekle (ikinci katman)
    noise2 = np.zeros_like(image, dtype=np.float32)
    for i in range(channels):
        noise2[:, :, i] = cv2.randn(np.zeros((height, width), dtype=np.float32), 0, 40 * intensity)

    grainy_image = cv2.add(grainy_image.astype(np.float32), noise2)
    grainy_image = np.clip(grainy_image, 0, 255).astype(np.uint8)

    if save_output:
        filename, ext = os.path.splitext(image_path)
        output_path = f"Outputs/Grain/{filename}_film_grain{ext}"

        # Çıktı klasörünü oluştur
        os.makedirs("Outputs/Grain", exist_ok=True)

        cv2.imwrite(output_path, grainy_image)
        print(f"Film grain effect applied image saved: {output_path}")

    return grainy_image