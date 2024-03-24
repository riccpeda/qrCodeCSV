import qrcode
import csv

strPath = str(input("Bitte geben Sie den Dateipfad mit Endung CSV an:"))

# Datei öffnen
with open(strPath, "r", encoding="UTF-8-SIG") as csvfile:

    # CSV-Reader-Objekt erstellen
    reader = csv.reader(csvfile, delimiter=';')
    next(reader, None)

    # Daten in Liste einlesen
    datenliste = []
    for zeile in reader:
        datenliste.append((zeile[0], zeile[1], zeile[2]))

# print(datenliste[0])


def make_qr(qrfilename, QRpath, msg):
    img = qrcode.make(msg)
    img.save(QRpath + "\\" + qrfilename)
    print(f"QR Code {qrfilename} saved")


for filename, url, qr_path in datenliste:
    # print(f"Filename: {filename}")
    # print(f"URL: {url}")
    make_qr(filename + ".png", qr_path, url)
