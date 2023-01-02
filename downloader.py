import requests

def download_video(url):
  link = f"https://ytdl.tiodevhost.my.id/?url={url}&filter=audioandvideo&quality=highestvideo&contenttype=video/mp4"
  response = requests.get(link)
  # Überprüfen Sie, ob die Anforderung erfolgreich war
  if response.status_code == 200:
    # Verarbeiten Sie den Inhalt der Antwort
    file_size = int(response.headers.get("Content-Length"))
    file_name = url.split("/")[-1] + ".mp4"

    # Öffnen Sie eine Datei zum Schreiben im Binary-Modus
    with open(file_name, "wb") as f:
      # Schreiben Sie den Inhalt der Antwort in die Datei
      f.write(response.content)

    print(f"Successfully downloaded {file_name} with size {file_size} bytes")
  else:
    print("Error downloading video")

def download_audio(url):
  link = f"https://ytdl.tiodevhost.my.id/?url={url}&filter=audioonly&quality=highestaudio&contenttype=audio/mpeg"
  response = requests.get(link)
  # Überprüfen Sie, ob die Anforderung erfolgreich war
  if response.status_code == 200:
    # Verarbeiten Sie den Inhalt der Antwort
    file_size = int(response.headers.get("Content-Length"))
    file_name = url.split("/")[-1] + ".mp3"

    # Öffnen Sie eine Datei zum Schreiben im Binary-Modus
    with open(file_name, "wb") as f:
      # Schreiben Sie den Inhalt der Antwort in die Datei
      f.write(response.content)

    print(f"Successfully downloaded {file_name} with size {file_size} bytes")
  else:
    print("Error downloading audio")
