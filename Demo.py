import os
import cv2

input_folder_path = "../VideoMinutes_Variasi_FPS/Testing"  # Replace with your input video folder path
output_folder_path = "../VideoMinutes_Variasi_FPS/Testing_2FPS"  # Replace with your output folder path"

# Set target FPS and frame numbers to capture
target_fps = 2
frames_per_second = 25
frames_to_capture = [1, 2]  # First frame and 12th frame of every second

# Calculate frame interval based on target FPS
frame_interval = int(frames_per_second / target_fps)

# Get list of input video files
input_files = os.listdir(input_folder_path)

# Process each video file
for file in input_files:
    # Construct input and output file paths
    input_file_path = os.path.join(input_folder_path, file)
    output_file_path = os.path.join(output_folder_path, file)

    # Open input video file
    input_video = cv2.VideoCapture(input_file_path)

    # Get video properties
    width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = input_video.get(cv2.CAP_PROP_FPS)
    total_frames = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create output video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video = cv2.VideoWriter(output_file_path, fourcc, target_fps, (width, height))

    # Initialize variables
    frame_number = 0
    captured_frames = 0

    while True:
        # Read the next frame from the input video
        ret, frame = input_video.read()

        # Check if frame was read successfully
        if not ret:
            break

        # Increment the frame number
        frame_number += 1

        # Check if the current frame number should be captured
        if frame_number % frame_interval in frames_to_capture:
            # Write the frame to the output video
            output_video.write(frame)
            captured_frames += 1

        # Break the loop if all the required frames have been captured
        if captured_frames == len(frames_to_capture) * (total_frames / frames_per_second):
            break

    # Release the video file readers and writers
    input_video.release()
    output_video.release()

    print(f"Video processing complete for {file}")

print("All videos processed.")
