% rebase('master.tpl', title='Teams')

<div class="container-fluid teams-container">
	<h3 class="container-header">Teams</h3>
	<div class="row">
		<div class="col-xs-6 col-xs-offset-3">

			<h4>Division I</h4>
			<ul>
			  % for team in teams:
			    <li><a href="/teams/{{team.name}}">{{team.name}}</a></li>
			  % end
			</ul>

		</div>
	</div>
</div>

