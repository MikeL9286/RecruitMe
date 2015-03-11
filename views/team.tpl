% rebase('master.tpl', title=team.name)

<div class="container-fluid teams-container">
	<h3 class="container-header">{{team.name}}</h3>
	<div class="row">
		<div class="centered">
			% if True:
			<form id="commit" action="/teams/{{team.name}}/commit" method="POST">
	            <button type="submit" class="btn btn-success">Commit</button>
          	</form>
			% else:
			<form id="decommit" action="/teams/{{team.name}}/decommit" method="POST">
				<button type="submit" class="btn btn-danger">Decommit</button>
			</form>
			% end
		</div>
		
		<div class="col-xs-6 col-xs-offset-3 commit-list">
			<h4 class="centered text-muted">Commits</h4>
			<div>
				% for commit in commits:
				<div>{{commit.name}}</div>
				% else:
				<div class="centered text-muted">{{team.name}} has no commits.</div>
				% end
			</div>
		</div>
	</div>
</div>

