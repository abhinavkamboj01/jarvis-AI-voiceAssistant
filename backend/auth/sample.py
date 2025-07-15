
import cv2
import os

# Create a video capture object
cam = cv2.VideoCapture(0)  #create a video capture object which is helpful to capture videos through webcam
cam.set(3, 640)  # set video FrameWidth
cam.set(4, 480)  # set video FrameHeight

# Check if camera opened successfully
if not cam.isOpened():
    print("❌ Error: Could not open camera. Check permissions or if it's in use.")
    exit()

# Load the Haar cascade
cascade_path = 'backend/auth/haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    print(f"❌ Error: Haar cascade file not found at: {cascade_path}")
    cam.release()
    exit()

detector = cv2.CascadeClassifier(cascade_path)
#Haar Cascade classifier is an effective object detection approach

# Get user ID
face_id = input("Enter a Numeric user ID here: ")
#Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)
print("📸 Taking samples, look at the camera...")

count = 0 # Initializing sampling face count

while True:
    ret, img = cam.read() #read the frames using the above created object

    if not ret or img is None:
        print("❌ Error: Failed to capture frame from camera.")
        break

    # Convert to grayscale
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #The function converts an input image from one color space to another

    # Detect faces
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  #used to draw a rectangle on any image
        count += 1

        sample_path = f"backend/auth/samples/face.{face_id}.{count}.jpg"
        cv2.imwrite(sample_path, converted_image[y:y+h, x:x+w])
        # To capture & Save images into the datasets folder
        cv2.imshow('image', img)  #Used to display an image in a window

    k = cv2.waitKey(100) & 0xff  # Waits for a pressed key
    if k == 27:
        print("🛑 ESC pressed. Exiting.")
        break
    elif count >= 100:   # Take 50 sample (More sample --> More accuracy)
        print("✅ Collected enough samples.")
        break

print("📂 Samples taken. Closing the program...")
cam.release()
cv2.destroyAllWindows()
