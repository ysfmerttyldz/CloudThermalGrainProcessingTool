import cv2

def convert_to_thermal(file_name):
    img = cv2.imread("Inputs/"+file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thermal = cv2.applyColorMap(blurred, cv2.COLORMAP_JET)

    cv2.imwrite('Outputs/Thermal/'+file_name, thermal)
    print("Thermal conversion completed successfully: Outputs/Thermal/"+file_name)
