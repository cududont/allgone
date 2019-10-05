import psutil
from time import sleep

process = "GTA5.exe"
gtapid = None

def main():
    for proc in psutil.process_iter():
        if proc.name() == process:
            procstr = str(proc)
            splitstr = procstr.split("=")[1]
            gtapid = splitstr.split(",")[0]

            print("Found GTA5 process with PID " + gtapid)

            p = psutil.Process(int(gtapid))
            print("Suspending process for 10 seconds...")
            p.suspend()
            sleep(10)
            print("Done")
            p.resume()

if __name__ == "__main__":
    main()

            
    
        