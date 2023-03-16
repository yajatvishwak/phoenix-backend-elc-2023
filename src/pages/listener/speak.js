// @ts-nocheck
let shutup = false;

function initVoice() {
  const voices = window.speechSynthesis.getVoices();
  if (voices.length === 0) {
    const voices = window.speechSynthesis.getVoices();
    const utterance = new SpeechSynthesisUtterance("");
    utterance.voice = voices.find(
      (voice) => voice.name === "Google UK English Male"
    );
    utterance.rate = 1;
    window.speechSynthesis.speak(utterance);
  }
}

function playDialogue(dialogue) {
  return new Promise((resolve, reject) => {
    const voices = window.speechSynthesis.getVoices();
    const utterance = new SpeechSynthesisUtterance(
      dialogue.replace(/<[^>]*>?/gm, "")
    );
    utterance.onend = () => resolve(true);
    utterance.onerror = (e) => reject(e);
    utterance.voice = voices.find(
      (voice) => voice.name === "Google UK English Male"
    );
    utterance.rate = 1;
    if (!shutup) {
      window.speechSynthesis.speak(utterance);
    }
  });
}
function stopDialogue() {
  window.speechSynthesis.cancel();
}

function playSound(sound) {
  const audio = new Audio(sound);
  audio.play();
}

export { playDialogue, stopDialogue, playSound, initVoice };
