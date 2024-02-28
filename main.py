from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def find_factors(number: int):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
        <html>
        <head>
            <title>Factor Finder</title>
            <script>
                function getFactors() {
                    const number = document.getElementById("number").value;
                    fetch(`/factors/${number}`)
                        .then(response => response.json())
                        .then(data => {
                            const factors = data.factors.join(', ');
                            document.getElementById("result").innerText = `Factors of ${data.number}: ${factors}`;
                        });
                }
            </script>
        </head>
        <body>
            <h1>Factor Finder</h1>
            <label for="number">Enter a number:</label>
            <input type="number" id="number" name="number" value="1">
            <button onclick="getFactors()">Find Factors</button>
            <div id="result"></div>
        </body>
        </html>
    """

@app.get("/factors/{number}")
async def get_factors(number: int):
    return {"number": number, "factors": find_factors(number)}
