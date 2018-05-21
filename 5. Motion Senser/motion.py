import cv2, time, pandas
from datetime import datetime

firstFrame = None
statusList = [None, None]
times=[]
df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

while True:
	check, frame = video.read()
	status = 0
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	if firstFrame is None:
		firstFrame = gray
		continue

	deltaFrame = cv2.absdiff(firstFrame, gray)

	threshFrame = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)[1]
	threshFrame = cv2.dilate(threshFrame, None, iterations = 2)

	(_, cnts, _) = cv2.findContours(threshFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for contour in cnts:
		if cv2.contourArea(contour) < 1000:
			continue
		status = 1
		(x, y, w, h) = cv2.boundingRect(contour)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
	statusList.append(status)
	statusList = statusList[-2:]
	if statusList[-1]==1 and statusList[-2] == 0:
		times.append(datetime.now())
	if statusList[-1]==0 and statusList[-2] == 1:
		times.append(datetime.now())
	
	cv2.imshow("Gray Frame",gray)
	cv2.imshow("Delta Frame", deltaFrame)
	cv2.imshow("Threshold Frame", threshFrame)
	cv2.imshow("Color Frame", frame)

	key = cv2.waitKey(5)

	if key==ord('q'):
		if status == 1:
			times.append(datetime.now())
		break

print(times)

for i in range(0, len(times), 2):
	df = df.append({"Start":times[i], "End": times[i+1]}, ignore_index=True)
df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows