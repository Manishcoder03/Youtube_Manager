import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}") 
    print("\n")
    print("*" * 70)

def add_video(videos):
    name =input("Enter video name: ")
    time =input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("enter the video number update"))
    if 1<=index <= len(videos):
        name=input("Enter the new video name: ")
        time=input("Enter the new video time: ")
        videos[index-1]={'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("invalid index number ")
        
    

def delete_video(videos):
    list_all_videos(videos)
    index= int(input("enter the video number to be deleted: "))
    if 1<=index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        
    else:
        print("invalid index number: ")
    

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choice an option ")
        print("1. list All youtube videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video  ")
        print("5. Exit the App")
        choice=input("enter Your Choice ")
        # print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("invalid choice")
        
 
if __name__ == "__main__":
    main()       