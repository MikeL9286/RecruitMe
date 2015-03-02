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
                    emailAddress: true
                }
            },
            password: {
                validators: {
                    notEmpty: true
                }
            },
            passwordCheck: {
            	validators: {
            		notEmpty: true,
            		identical: {
            			field: 'password',
            			message: 'The passwords do not match.'
            		}
            	}
            }
        }
	});
});