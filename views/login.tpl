% rebase('master.tpl', title='Login')

<div class="container-fluid">
  <div class="row">
    <div class="col-xs-3 col-xs-offset-4">

      % setdefault('email', '')
      % setdefault('password', '')
      % setdefault('error', '')
      <div class="panel">
        <h3 class="panel-heading">Log in</h3>
        <div class="panel-body">
          <form action="login" method="POST">
            <div class="form-group">
              <label for="email" class="sr-only">E-mail</label>
              <input id="email" name="email" placeholder="E-mail" value="{{email}}" class="form-control" />
            </div>
            <div class="form-group">
              <label for="password" class="sr-only">Password</label>
              <input name="password" placeholder="Password" value="{{password}}" class="form-control" />
            </div>
            <div class="form-group">    
              <button type="submit" class="btn btn-default">Log in</button>
            </div>
            <div class="form-group">
              <label class="text-danger">{{error}}</label>
            </div>
          </form>
        </div>
        <h5 class="panel-footer">Don't have an account? <a href="/signup">Sign up</a></h5>
      </div>

    </div>
  </div>
</div>

<script>
  $.backstretch("/images/splash1.jpg");
</script>