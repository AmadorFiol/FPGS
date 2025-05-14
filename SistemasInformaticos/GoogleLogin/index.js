const express = require("express");
const session = require("express-session");
const passport = require("passport");
const GoogleStrategy = require("passport-google-oauth20").Strategy;
require("dotenv").config()
/*
GGL_CLI_ID -> ID cliente google
GGL_CLI_SCRT -> Secreto cliente google
SESSION_SCRT -> Secreto sesion
*/

const app = express();

app.use(session({
  secret: process.env.SESSION_SCRT,
  resave: false,
  saveUninitialized: false,
}));

app.use(passport.initialize());
app.use(passport.session());

// Serializar y deserializar usuario
passport.serializeUser((user, done) => done(null, user));
passport.deserializeUser((user, done) => done(null, user));

// Configurar estrategia de Google
passport.use(new GoogleStrategy({
  clientID: process.env.GGL_CLI_ID,
  clientSecret: process.env.GGL_CLI_SCRT,
  callbackURL: "/auth/google/callback",
}, (accessToken, refreshToken, profile, done) => {
  return done(null, profile);
}));

// Rutas
app.get("/", (req, res) => {
  if (req.isAuthenticated()) {
    res.send(`<h1>Bienvenido, ${req.user.displayName}</h1><a href="/logout">Cerrar sesión</a>`);
  } else {
    res.send('<a href="/auth/google">Iniciar sesión con Google</a>');
  }
});

app.get("/auth/google",
  passport.authenticate("google", {
    scope: ["profile", "email"],
    prompt: "select_account"
  })
);


app.get("/auth/google/callback",
  passport.authenticate("google", { failureRedirect: "/" }),
  (req, res) => {
    res.redirect("/");
  }
);

app.get("/logout", (req, res) => {
  req.logout(() => {
    res.redirect("/");
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor en http://localhost:${PORT}`));
