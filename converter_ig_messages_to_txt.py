import json, msvcrt
import datetime as dt


def readInstagramMessage(path, filename, order, outputfilename):

    with open(f"{path}\{filename}.json") as file:
        data = json.load(file)

    output_file = f"{path}/{outputfilename}.txt"  # Specify the path and filename for the output file

    with open(output_file, "w", encoding="utf-8") as f:
        df = []
        if order == "0":
            df = reversed(data["messages"])
        else:
            df = data["messages"]
        for message in df:
            temp = ''
            try:
                sender_name = message.get("sender_name", "Unknown Sender")
                timestamp_ms = message.get("timestamp_ms", 0)
                content = message.get("content", "")

                if content:
                    temp = content

                timestamp = dt.datetime.fromtimestamp(timestamp_ms / 1000)  # Convert milliseconds to seconds
                f.write("\nTime: " + timestamp.strftime('%Y-%m-%d %H:%M:%S') + "\n")
                f.write("Sender: " + sender_name + "\n")
                if content:
                    f.write("Message: " + temp + "\n")
                else:
                    f.write("(Attachment)\n")
            except KeyError:
                f.write("Missing key in message!\n")
                continue
        print("Output file has been created successfully!")

        print("Press any key to exit...")
        msvcrt.getch()


path = input("Enter the path of the file: ")
filename = input("Enter the filename [default is: message_1][Only JSON file, not  including .json]: ")
order = input("Enter the order of the messages [0-Oldest to Newest][1-Newest to Oldest]: ")
outputfilename = input("Enter the output filename [Only TXT file, not including .txt]: ")

print("Reading Instagram Message...")
print("Output will be in the same folder as the input file. Please wait.")

readInstagramMessage(path, filename, order, outputfilename)
