% rebase('master.tpl', title='Welcome')

<div class="container-fluid">
  <div class="row">
    <div class="col-xs-3 col-xs-offset-4">

    	<div class="panel">
    	<div class="panel-body">
			<div>Welcome {{user.full_name}}</div>
			<div>Email: {{user.email}}</div>
			<div>Password: {{user.password}}</div>
			<div>Role: {{user.role.name}}</div>
		</div>
		</div>

		<div>
			<h3>TODO</h3>
			members
			.recruiters
			.recruits

			groups

			notifications
			.messages
		</div>

	</div>
  </div>
</div>