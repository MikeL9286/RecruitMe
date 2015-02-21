% rebase('master.tpl', title='Login')

<div class="container-fluid">
  <div class="row">
    <div class="col-xs-3 col-xs-offset-4">

      % setdefault('loginEmail', '')
      % setdefault('loginPassword', '')
      % setdefault('loginError', '')
      <form action="login" method="POST" class="form-login">
        <div class="form-group">
          <label>Log in</label>
        </div>
        <div class="form-group">
          <label for="email" class="sr-only">E-mail</label>
          <input id="email" name="email" placeholder="E-mail" value="{{loginEmail}}" class="form-control" />
        </div>
        <div class="form-group">
          <label for="password" class="sr-only">Password</label>
          <input name="password" placeholder="Password" value="{{loginPassword}}" class="form-control" />
        </div>
        <div class="form-group">    
          <button type="submit" class="btn btn-default">Log in</button>
        </div>
        <div class="form-group">
          <label class="text-danger">{{loginError}}</label>
        </div>
      </form>

      % setdefault('signUpFullName', '')
      % setdefault('signUpEmail', '')
      % setdefault('signUpPassword', '')
      % setdefault('signUpPasswordCheck', '')
      % setdefault('signUpError', '')
      <form action="signUp" method="POST" class="form-sign-up">
        <div class="form-group">
          <label>Don't have an account? <span class="text-muted">Sign up</span></label>
        </div>
        <div class="form-group">
          <label for="fullName" class="sr-only">Full Name</label>
          <input id="fullName" name="fullName" placeholder="Full Name" value="{{signUpFullName}}" class="form-control" />
        </div>
        <div class="form-group">
          <label for="email" class="sr-only">E-mail</label>
          <input id="email" name="email" placeholder="E-mail" value="{{signUpEmail}}" class="form-control" />
        </div>
        <div class="form-group">
          <label for="password" class="sr-only">Password</label>
          <input name="password" placeholder="Password" value="{{signUpPassword}}" class="form-control" />
        </div>
        <div class="form-group">
          <label for="passwordCheck" class="sr-only">Verify Password</label>
          <input name="passwordCheck" placeholder="Verify Password" value="{{signUpPasswordCheck}}" class="form-control" />
        </div>
        <div class="form-group">    
          <button type="submit" class="btn btn-default">Sign up</button>
        </div>
        <div class="form-group">
          <label class="text-danger">{{signUpError}}</label>
        </div>
      </form>

    </div>
  </div>
</div>