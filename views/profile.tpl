% rebase('master.tpl', title='Welcome')

<div class="container-fluid">
	<div class="row">  		
		<div class="profile-container col-xs-8 col-xs-offset-2">
		
			<h3 class="profile-header">Update Your Profile</h3>

			<div class="row">
				<div class="col-xs-6 col-xs-offset-3">
					<form action="update_email" method="PUT">
				    	<div class="form-group">
				    		<label for="email">Change your e-mail</label>
				    		<input id="email" name="email" placeholder="E-mail" value="{{user.email}}" class="form-control" />
				    	</div>
			    	</form>	
	    		</div>
	    	</div>
	    	
	    	<div class="row">
	    		<div class="col-xs-6 col-xs-offset-3">
			    	<form action="update_password" method="PUT">
			    		<label>Change your password</label>
				    	<div class="form-group">
				    		<label for="oldPassword" class="sr-only">Old Password</label>
				    		<input id="oldPassword" name="oldPassword" class="form-control" placeholder="Old Password" />
				    	</div>
				    	<div class="form-group">
				    		<label for="oldPassword" class="sr-only">New Password</label>
				    		<input id="newPassword" name="newPassword" class="form-control" placeholder="New Password" />
				    	</div>
				    	<div class="form-group">
				    		<label for="oldPassword" class="sr-only">Verify Your Password</label>
				    		<input id="passwordCheck" name="passwordCheck" class="form-control" placeholder="Verify New Password" />
				    	</div>
			    	</form>
	    		</div>
	    	</div>

	    	<div class="row">
	    		<div class="col-xs-6 col-xs-offset-3">
			    	<form action="update_name" method="PUT">
			    		<label>Update Your Name</label>
			    		<div><em>This is the name that others will see when they view your profile.</em></div>
				    	<div class="form-group">
				    		<label for="name" class="sr-only">Full Name</label>
				    		<input id="name" name="name" class="form-control" placeholder="Full Name" value="{{user.full_name}}" />
				    	</div>
			    	</form>
	    		</div>
	    	</div>
		
		</div>
	</div>

	<br/>
	<br/>
	<div>
		<div class="panel">
	    	<h3 class="panel-heading">User Info for Debug</h3>
	    	<div class="panel-body">
	    		<p>Name: {{user.full_name}}</p>
	    		<p>Email: {{user.email}}</p>
	    		<p>Pass: {{user.password}}</p>
	    		<p>Role: {{user.role.name}}</p>
	    	</div>
	    </div>
	</div>

</div>