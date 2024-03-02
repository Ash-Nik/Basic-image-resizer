import cv2

# configurable parameters
source = "KRISNA.jpg"
destination = "newImage.jpeg"
scale_Percentage = 150
# calculate 40% of original image
# percentage which image is resized

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
new_Width = int(src.shape[1] * scale_Percentage / 100)  # 1 is used for width
new_Height = int(src.shape[0] * scale_Percentage / 100)  # 0 is used for height
output = cv2.resize(src, (new_Height, new_Height))

# writing resized image
cv2.imwrite(destination, output)
cv2.waitKey(0)
