$(document).ready(function() {
	$('form#login').formValidation({
		framework: 'bootstrap',
        icon: {
            valid: 'fa fa-check',
            invalid: 'fa fa-remove',
            validating: 'fa fa-spinner'
        },
        fields: {
            email: {
                validators: {
                    notEmpty: true,
                    emailAddress: true
                }
            },
            password: {
                validators: {
                    notEmpty: true
                }
            }
        }
	});
});