/*
Function required for EmailJS to work as required.  Links the values in the form to the EmailJS template and variables
and defines 'success' and 'failed' response.
*/
function sendMail(contactForm) {
    emailjs.send("Gmail", "community-treats", {
        "from_name": contactForm.name.value,
        "reply_to": contactForm.email.value,
        "message": contactForm.feedback.value
      })
      .then(
        function (response) {
          alert("Message successfully sent.  We appreciate your feedback!");
        },
        function (error) {
          alert("Message not sent, please try again. if problem persists please check your network settings");
        }
      );
    return false; //blocks a new page from loading.
  }