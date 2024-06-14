const form = document.getElementById('depression-test-form');
const scoreEl = document.getElementById('score');
const resultEl = document.getElementById('result');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  let totalScore = 0;
  const questions = document.querySelectorAll('.question');

  // Loop through each question and calculate total score
  for (const question of questions) {
    const selectedOption = question.querySelector('input[name="q1"]:checked');
    if (selectedOption) {
      totalScore += parseInt(selectedOption.value);
    }
  }

  // Display result based on score (you can adjust the ranges and messages)
  scoreEl.textContent = `Your score is: ${totalScore}`;
  if (totalScore < 10) {
    scoreEl.textContent += " - You might not be experiencing significant depression.";
  } else if (totalScore < 20) {
    scoreEl.textContent += " - You might be experiencing some symptoms of depression. Consider seeking professional help if these feelings persist.";
  } else {
    scoreEl.textContent += " - You might be experiencing moderate to severe depression. Consider seeking professional help as soon as possible.";
  }

  resultEl.style.display = 'block';
});
