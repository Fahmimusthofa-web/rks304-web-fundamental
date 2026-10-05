// Validasi input form register (event handling: submit, input, blur)

const form = document.getElementById("form-register");

// Aturan validasi tiap field. Mengembalikan pesan error, atau "" jika valid.
const aturan = {
  username: (v) => {
    if (v.trim() === "") return "Username tidak boleh kosong.";
    if (v.trim().length < 3) return "Username minimal 3 karakter.";
    return "";
  },
  password: (v) => {
    if (v === "") return "Password tidak boleh kosong.";
    if (v.length < 8) return "Password minimal 8 karakter.";
    return "";
  },
  nama: (v) => (v.trim() === "" ? "Nama tidak boleh kosong." : ""),
  tanggal_lahir: (v) => {
    if (v === "") return "Tanggal lahir tidak boleh kosong.";
    // Format input date (YYYY-MM-DD) bisa dibandingkan langsung sebagai string.
    const d = new Date();
    const hariIni = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
    if (v > hariIni) return "Tanggal lahir tidak boleh di masa depan.";
    return "";
  },
  alamat: (v) => (v.trim() === "" ? "Alamat tidak boleh kosong." : ""),
  telepon: (v) => {
    if (v.trim() === "") return "Nomor telepon tidak boleh kosong.";
    if (!v.trim().startsWith("62")) return "Nomor telepon harus diawali 62.";
    return "";
  },
};

// Tampilkan / hapus pesan error di bawah input
function tampilkanError(input, pesan) {
  const el = input.parentElement.querySelector(".error");
  el.textContent = pesan;
  el.classList.toggle("hidden", pesan === "");
  input.classList.toggle("border-red-500", pesan !== "");
  input.classList.toggle("border-stone-300", pesan === "");
}

function validasiField(input) {
  const pesan = aturan[input.name](input.value);
  tampilkanError(input, pesan);
  return pesan === "";
}

// Validasi langsung saat mengetik / berpindah field
Object.keys(aturan).forEach((nama) => {
  const input = form.elements[nama];
  input.addEventListener("input", () => validasiField(input));
  input.addEventListener("blur", () => validasiField(input));
});

// Validasi semua field saat submit; batalkan submit jika ada yang salah
form.addEventListener("submit", (e) => {
  let semuaValid = true;
  Object.keys(aturan).forEach((nama) => {
    if (!validasiField(form.elements[nama])) semuaValid = false;
  });
  if (!semuaValid) e.preventDefault();
});
