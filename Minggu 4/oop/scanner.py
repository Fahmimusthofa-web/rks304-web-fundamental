# oop/scanner.py
import socket
import sys
from datetime import datetime
from abc import ABC, abstractmethod

class BaseScanner(ABC):
    """Kerangka dasar untuk pemindai jaringan (Abstraksi)"""
    
    def __init__(self, target_host, start_port, end_port):
        # Enkapsulasi data
        self._target_host = target_host
        self._start_port = start_port
        self._end_port = end_port
        self._target_ip = self._resolve_host()
        self._open_ports = []

    def _resolve_host(self):
        try:
            return socket.gethostbyname(self._target_host)
        except socket.gaierror:
            print("\n[!] Host tidak dapat diselesaikan. Periksa kembali nama/IP target.")
            sys.exit(1)

    @abstractmethod
    def scan(self, timeout=0.5):
        pass
    
    # Getter untuk mengakses data (menjaga enkapsulasi)
    @property
    def target_host(self): return self._target_host
    @property
    def target_ip(self): return self._target_ip
    @property
    def start_port(self): return self._start_port
    @property
    def end_port(self): return self._end_port
    @property
    def open_ports(self): return self._open_ports

class TCPPortScanner(BaseScanner):
    """Implementasi konkrit untuk pemindaian protokol TCP"""
    
    def scan(self, timeout=0.5):
        print("-" * 50)
        print(f" Memindai Target IP: {self.target_ip}")
        print(f" Rentang Port      : {self.start_port} - {self.end_port}")
        print(f" Waktu Mulai       : {str(datetime.now())}")
        print("-" * 50)

        try:
            for port in range(self.start_port, self.end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(timeout)
                result = s.connect_ex((self.target_ip, port))
                s.close()

                if result == 0:
                    print(f"[+] Port {port} : TERBUKA")
                    self._open_ports.append(port)
        except KeyboardInterrupt:
            print("\n[!] Pemindaian dibatalkan oleh pengguna (Ctrl+C).")

        print("-" * 50)
        print(f" Pemindaian Selesai. Total port terbuka ditemukan: {len(self.open_ports)}")
        print("-" * 50)
        
        return self.open_ports