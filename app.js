const additionForm = document.getElementById("addition-form");
const firstNumberInput = document.getElementById("first-number");
const secondNumberInput = document.getElementById("second-number");
const thirdNumberInput = document.getElementById("third-number");
const result = document.getElementById("result");

additionForm.addEventListener("submit", async (event) => {
	event.preventDefault();

	try {
		const response = await fetch("/add", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				first: firstNumberInput.value,
				second: secondNumberInput.value,
				third: thirdNumberInput.value,
			}),
		});

		if (!response.ok) {
			throw new Error("การคำนวณไม่สำเร็จ");
		}

		const data = await response.json();
		result.textContent = `ผลรวม: ${data.result}`;
	} catch (error) {
		const firstNumber = Number(firstNumberInput.value);
		const secondNumber = Number(secondNumberInput.value);
		const thirdNumber = Number(thirdNumberInput.value);
		result.textContent = `ผลรวม: ${firstNumber + secondNumber + thirdNumber}`;
	}
});