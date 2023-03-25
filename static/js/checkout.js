// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys

const stripe = Stripe('pk_test_51MpL6FG4DY3biWn4lJxPf1gsnBTTaJVU0f6FOuLHP3F0jPR33WIOx6twS5VKy9W3J0vBOr4y2GhnpAo6neaKGzFy000oIcOu1d');

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained only the payment

//The payment element renders a dynamic form that allows the customer to pick a payment method
//Depending on the payment method, the form automatically requests that the customer fills
//in all necessary payment details

var elements = stripe.elements();
// Add some style from react
var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px',
    }
};

// Create and mount the Payment Element
//The payment element can be customized to match the design of the site by passing the appearance object
// options when creating the elements provider
var card = elements.create('card', { style: style });
card.mount("#card-element");


// If their is an error stripe will display an error with block styling 
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


//Collect the information in the form with event listener

var form = document.getElementById('payment-form')

form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // collect the information from the form organize it into a data structure
    var custName = document.getElementById("custName").value;
    var custAdd = document.getElementById("custAdd").value;
    var custAdd2 = document.getElementById("custAdd2").value;
    var postCode = document.getElementById("postCode").value;

    //Perform a stripe confirm Card payment using details from the payment Element.  
    //Provide a return_url to this function to indicate where Stripe should redirect
    //user after they complete the payment. 
    stripe.confirmCardPayment(clientsecret, {
        //payment form data structure
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
        // This point will only be reached if there is an immediate error when
        // confirming the payment. Show error to your customer (for example, payment
        // details incomplete)

        if (results.error) {
            console.log('payment error')
            console.log(result.error.message);

            // const messageContainer = document.querySelector('#error-message');
            // messageContainer.textContent = error.message;

        }else {
        // Your customer will be redirected to your `return_url`. For some payment
        // methods like iDEAL, your customer will be redirected to an intermediate
        // site first to authorize the payment, then redirected to the `return_url`.
            if (result.paymentIntent.status == 'succeeded') {
                console.log('payment processed')
                // There's a risk of the customer closing the window before callback
                // execution. Set up a webhook or plugin to listen for the
                // payment_intent.succeeded event that handles any business critical
                // post-payment actions.


                //Make sure the return url corresponds to a page on your website
                //that provides teh status of the payment.  
                //When stripe redirects the customer to the return url, stripe
                // provides the following URL query parameters
                // payment_intent: The unique identifier for the PaymentIntent
                // payment_intent_client_secret: The client secret of the paymentIntent Object
                window.location.replace("https://example.com/order/123/complete");
                // window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");


                /*
                NOTE: If you have tooling that tracks the customer’s browser session, 
                ou might need to add the stripe.com domain to the referrer exclude list. 
                Redirects cause some tools to create new sessions, which prevents you from 
                tracking the complete session.
                */
            }
        }
    });

});