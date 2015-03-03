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
                threshhold: 3,
                verbose: false,
                validators: {
                    notEmpty: true,
                    emailAddress: true,
                    remote: {
                        message: 'This email is already in use.',
                        url: '/validate-email',
                        type: 'POST',
                        data: function(validator) {
                            return {
                                email: validator.getFieldElements('email').val()
                            };
                        },
                        delay: 500
                    }
                }
            }
        }
	});

    $('form#update-password').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'fa fa-check',
            invalid: 'fa fa-remove',
            validating: 'fa fa-spinner'
        },
        fields: {
            oldPassword: {
                validators: {
                    notEmpty: true
                    
                }
            },
            newPassword: {
                validators: {
                    notEmpty: true,
                    different: {
                        field: 'oldPassword'
                    },
                    callback: {
                        callback: function (value, validator, $field) {
                            var password = validator.getFieldElements('newPassword').val();
                            return validatePasswordRequirements(password);
                        }
                    }
                }
            },
            passwordCheck: {
                validators: {
                    notEmpty: true,
                    identical: {
                        field: 'newPassword'
                    }
                }
            }
        }
    });

    $('form#update-name').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'fa fa-check',
            invalid: 'fa fa-remove',
            validating: 'fa fa-spinner'
        },
        fields: {
            name: {
                validators: {
                    notEmpty: true
                }
            }
        }
    });
});