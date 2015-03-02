$(document).ready(function() {
	$('form#update-email').formValidation({
		framework: 'bootstrap',
        icon: {
            valid: 'fa fa-check',
            invalid: 'fa fa-remove',
            validating: 'fa fa-spinner'
        },
        fields: {
            email: {
                validators: {
                    notEmpty: true
                }
            }
        }
	});
});