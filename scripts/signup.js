$(document).ready(function() {
	$('form#signup').formValidation({
		framework: 'bootstrap',
        icon: {
            valid: 'fa fa-check',
            invalid: 'fa fa-remove',
            validating: 'fa fa-spinner'
        },
        fields: {
        	fullName: {
        		validators: {
        			notEmpty: true
        		}
        	},
            email: {
                validators: {
                    notEmpty: true,
                    emailAddress: true,
                    remote: {
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
            },
            password: {
                validators: {
                    notEmpty: true,
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
            			field: 'password'
            		}
            	}
            }
        }
	});
});