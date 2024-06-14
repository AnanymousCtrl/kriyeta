
function calculateScore() {
    let form = document.forms['depressionTestForm'];
    let score = 0;
    for (let i = 1; i <= 16; i++) {
        let value = form['q' + i].value;
        score += parseInt(value);
    }

    let recommendation = "";

    if (score >= 0 && score <= 5) {
        recommendation = "Minimal depression. Suggestions: Maintain a healthy lifestyle, engage in social activities.";
    } else if (score > 5 && score <= 10) {
        recommendation = "Mild depression. Suggestions: Consider therapy, practice mindfulness.";
    } else if (score > 10 && score <= 15) {
        recommendation = "Moderate depression. Suggestions: Therapy is recommended, possibly medication.";
    } else if (score > 15 && score <= 20) {
        recommendation = "Moderately severe depression. Suggestions: Seek medical advice, medication likely needed.";
    } else if (score > 20 && score <= 28) {
        recommendation = "Severe depression. Suggestions: Immediate therapy required, consult Psychologist.";
    } else if (score > 28 && score <= 48) {
        recommendation = "Clinical  depression. Suggestions: Immediate medical attention required, intensive treatment.";
    }

    document.getElementById('result').innerText = "Your total score is: " + score + "\n" + recommendation;
}