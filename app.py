# https://youtu.be/l3QVYnMD128

from flask import Flask, request, render_template
import pickle

# Create an app object using the Flask class.
app = Flask(__name__)

# Load the trained model. (Pickle file)
model = pickle.load(open('Models\\eyclass.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('test.html')


@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['file']
    # features = np.array(int_features) #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(image)  # features Must be in the form [[a, b]]

    output = round(prediction[0], 2)

    return render_template('test.html', prediction_text='Percent with heart disease is {}'.format(output))


if __name__ == "__main__":
    app.run()
