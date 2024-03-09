# Import necessary libraries
from azure.iot.device import IoTHubDeviceClient, Message
import time
import json
import random

# Define connection string for IoT Hub
connection = "HostName=sensors-data-IoT.azure-devices.net;DeviceId=sensors-device-IoT;SharedAccessKey=WFkelOB+AMBh/BgU5FlGJ7CAr4rDXWXecAIoTGjgpzo="

def main():
    try:
        # Create IoT Hub device client
        client = IoTHubDeviceClient.create_from_connection_string(connection)
        
        # Main loop to send data to IoT Hub
        while True:
            # Generate random data
            data = {
                "DeviceID": random.randint(1, 100),
                "DeviceNumber": random.randint(1, 100),
                "Temperature": round(random.uniform(20, 30), 2),  # Temperature in Celsius
                "Humidity": round(random.uniform(40, 60), 2),     # Humidity in percentage
                "Pressure": round(random.uniform(800, 1200), 2),  # Pressure in hPa
                "Location": "Room-" + str(random.randint(1, 10)),  # Location of the device
                "Status": random.choice(["Online", "Offline"])     # Status of the device
            }
            
            # Create message from JSON data
            message = Message(json.dumps(data))
            
            # Send message to IoT Hub
            client.send_message(message)
            
            # Print success message
            print(f"Message {message} was sent successfully")
            
            # Wait for 2 seconds before sending next message
            time.sleep(2)
    
    # Handle keyboard interrupt
    except KeyboardInterrupt:
        print("Program was interrupted")

# Entry point of the script
if __name__ == "__main__":
    main()
