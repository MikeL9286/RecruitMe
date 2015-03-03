% rebase('master.tpl', title='team.name')

<div class="container-fluid teams-container">
	<h3 class="container-header">{{team.name}}</h3>
	<div class="row">
		<div class="col-xs-6 col-xs-offset-3">

			% if True:
				<button class="btn btn-default">Commit</button>
			% else:
				<button class="btn btn-default">Decommit</button>
			% end
			
			<h4>Commits</h4>
			None

		</div>
	</div>
</div>

