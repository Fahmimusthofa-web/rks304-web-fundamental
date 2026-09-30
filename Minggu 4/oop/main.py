# oop/main.py
import sys
from scanner import TCPPortScanner
from report import PDFReportExporter, JSONReportExporter

def main():
    print("=== APLIKASI PORT SCANNER & EXPORTER (OOP) ===")
    target = input("Masukkan IP atau Domain target (contoh: 127.0.0.1): ").strip()
    
    try:
        start = int(input("Masukkan port awal (contoh: 1): "))
        end = int(input("Masukkan port akhir (contoh: 1024): "))
    except ValueError:
        print("[!] Masukkan angka port yang valid.")
        sys.exit(1)

    # 1. Inisialisasi Objek Scanner & Mulai Scan
    scanner = TCPPortScanner(target, start, end)
    scanner.scan(timeout=0.4)
    
    # 2. Persiapan Penamaan File Output
    safe_target = target.replace('.', '_')
    pdf_filename = f"scan_report_{safe_target}.pdf"
    json_filename = f"scan_report_{safe_target}.json"

    # 3. Inisialisasi Objek Report (Memasukkan instance 'scanner' ke dalam exporter)
    pdf_report = PDFReportExporter(scanner, pdf_filename)
    json_report = JSONReportExporter(scanner, json_filename)

    # 4. Eksekusi Ekspor lewat Polimorfisme
    pdf_report.export()
    json_report.export()

if __name__ == "__main__":
    main()