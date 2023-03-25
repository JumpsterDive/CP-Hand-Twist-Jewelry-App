var stripe = Stripe{ sk_test_51MpL6FG4DY3biWn460Tdt3qUUVqUorCebaQSFpfSyRZyRzQ5Dul0Zhz84vAo2RbeW9lr1ZUpdh0MJtU5wqAhHgzu00O1jKpM7L }


var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

//Setup Stripe Elements in the payment form

var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px',
    }
};

// Build the elements from the predefined elements
var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function (event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info');
    }
});


//Capture the information in the form

var form = document.getElementById('payment-form')

form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // collect the information from the form organize it into a data structure
    var custName = document.getElementById("custName").value;
    var custAdd = document.getElementById("custAdd").value;
    var custAdd2 = document.getElementById("custAdd2").value;
    var postCode = document.getElementById("postCode").value;
    //Send the payment
    stripe.confirmCardPayment(clientsecret, {
        payment_method: {
            card: card,
            billing_details: {
                address: {
                    line1: custAdd,
                    line2: custAdd2
                },
                name: custName
            },
        }
        //Confirm the payment was successfully recieved
    }).then(function(results){
        if (results.error) {
            console.log('payment error')
            console.log(result.error.message);

        }else {
            if (result.paymentIntent.status === 'succeeded') {
                console.log('payment processed')
                // There's a risk of the customer closing the window before callback
                // execution. Set up a webhook or plugin to listen for the
                // payment_intent.succeeded event that handles any business critical
                // post-payment actions.
                window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
            }
        }
    });

});