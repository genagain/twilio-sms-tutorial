from flask import Flask
import twilio.twiml

app = Flask(__name__)

callers = {
    "+12038485151": "Paulina",
    "+13479860720": "Gen",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
  """Respond and greet the caller by name."""
  from_number = request.values.get('From', None)
  if from_number in callers:
    message = callers[from_number] + ", thanks for the message!"
  else:
    message = "Monkey, thanks for the message!"

  resp = twilio.twiml.Response()
  return str(resp)

if __name__ == "__main__":
  app.run(debug=True)
