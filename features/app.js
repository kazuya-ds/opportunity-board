/**
 * Professional Opportunity Board Logic
 */

// Theme Management
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark' : 'light');
}

// Text to Speech
let isSpeechEnabled = false;
function toggleSpeech() {
    isSpeechEnabled = !isSpeechEnabled;
    const btn = document.getElementById('speech-btn');
    btn.innerText = isSpeechEnabled ? "Disable Speech" : "Enable Speech";
}

document.addEventListener('mouseover', (e) => {
    if (isSpeechEnabled && e.target.closest('.listing-item')) {
        const text = e.target.closest('.listing-item').innerText;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(new SpeechSynthesisUtterance(text));
    }
});

// CSV Export (NASA Open Science Compliance)
function exportToCSV() {
    const data = [
        ["Opportunity", "Sponsor", "Deadline", "Stipend"],
        ["IoT4Ag Summer Internship", "UC Merced / IoT4Ag", "March 16, 2026", "$8,000"]
    ];
    let csv = "data:text/csv;charset=utf-8," + data.map(e => e.join(",")).join("\n");
    const link = document.createElement("a");
    link.href = encodeURI(csv);
    link.download = "ucm_opportunities.csv";
    link.click();
}

// Preference Load
if (localStorage.getItem('theme') === 'dark') document.body.classList.add('dark-mode');