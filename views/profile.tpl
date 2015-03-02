% rebase('master.tpl', title='Profile')

<div class="container-fluid profile-container">
	<h3 class="profile-header">Update Your Profile</h3>
	<div class="row">
		<div class="col-xs-6 col-xs-offset-3">

			<form id="update-email" action="update-email" method="POST" class="panel-form">
		    	<div class="form-group">
		    		<label for="email" class="text-muted">Update your e-mail</label>
		    		<input id="email" name="email" placeholder="E-mail" value="{{user.email}}" class="form-control" />
		    	</div>
		    	<button type="submit" class="btn btn-default"><i class="fa fa-edit"></i> Update</button>
	    	</form>	
	
	    	<form id="update-email" action="update-password" method="PUT" class="panel-form">
	    		<label class="text-muted">Update your password</label>
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
		    	<button type="submit" class="btn btn-default"><i class="fa fa-edit"></i> Update</button>
	    	</form>

	    	<form action="update-name" method="PUT" class="panel-form">
	    		<label class="text-muted">Update Your Name</label>
	    		<div class="form-description">
	    			<i class="fa fa-question"></i> <small>This is the name that others will see when they view your profile.</small>
	    		</div>
		    	<div class="form-group">
		    		<label for="name" class="sr-only">Full Name</label>
		    		<input id="name" name="name" class="form-control" placeholder="Full Name" value="{{user.full_name}}" />
		    	</div>
		    	<button type="submit" class="btn btn-default"><i class="fa fa-edit"></i> Update</button>
	    	</form>

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

<script src="/scripts/profile.js"></script>