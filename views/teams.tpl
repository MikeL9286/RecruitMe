% rebase('master.tpl', title='Teams')

<div class="container-fluid teams-container">
	<h3 class="container-header">Teams</h3>
	<div class="row">
		<div class="col-xs-12 col-sm-8 col-sm-offset-2">

			<h4 class="container-header">Division I</h4>
			% for conf in conferences:
			<div class="col-xs-10 col-xs-offset-1 col-sm-4 col-sm-offset-0 centered">
				<h4 class="text-muted">{{conf['name']}}</h4>
				<ul class="list-unstyled">
			    	% for team in conf['teams']:
			    	<li><a href="/teams/{{team.name}}">{{team.name}}</a></li>
			    	% end
			    </ul>
		    </div>
		  	% end

		</div>
	</div>
</div>