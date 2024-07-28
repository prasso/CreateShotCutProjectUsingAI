#chmod +x scripts.sh
tts --text "Introduction to Prasso" --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 01.wav

tts --text "Prasso is a robust platform designed to support multi-tenant applications. Built with Laravel, it utilizes and extends Laravel Teams, offering enhanced capabilities such as sub-teams within each team." --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 02.wav

tts --text "Prasso is a platform that streamlines the app prototype process for owners by providing a wizard-like framework for gathering the necessary details and building custom mobile and web apps.
With Prasso, you can create both your app API backend and your website with one setup form. You can then use the admin tools to customize these with branding and content." --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 03.wav

tts --text "Key Concepts" --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 04.wav

tts --text "Users and Teams" --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 05.wav

tts --text "- Users belong to teams. Users can be invited to a team or can own their own private team.
- When a user registers, a private team is assigned. Users can also be included in other teams.
- A team owner is one who has been assigned to admin a team or who has created the team.
- Teams are the basic unit in a social group. Teams have owners (coaches) and members." --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 06.wav

tts --text "Roles
- Users have roles. There are three tiers of user roles: Super-Admin, Site Admin, and App User.
- Allow anyone with a login to log into the app. No role is required.
- Site-admins can log into the sites they have an association with.
- Super-admins can access any site admin area." --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 07.wav

tts --text "Sites
- Teams own sites. Everything is based on a site.
- A site is determined by its URL and has assigned attributes that determine the appearance of the site.
- A Prasso site is both a business information site and a Prasso API site. The API serves the Prasso apps.
- Sites have site pages. These can be created and maintained using a built-in visual editor based on the GrapesJS opensource project.
- Sites are the landing page of the App home website. Example Prasso sites: [https://prasso.io](https://prasso.io/), [https://barimorphosis.com](https://barimorphosis.com/), [https://lileyscapes.prasso.io](https://lileyscapes.prasso.io/), [https://mercyfullfarms.com](https://mercyfullfarms.com/)" --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 08.wav

tts --text "Apps
- Sites can have an APP. When a user who is a member of a team logs into the Prasso app, the default-designated app will be loaded for use.
- Apps have an association to a site.
- An app is configured with tabs that point to views.
- An app is identified at the backend by the host of the request.
- The host is associated with the site, the site is associated with the app." --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 09.wav

tts --text "Tabs
- Apps have tabs. Users "build" their apps in the Prasso Admin tool.
- App tabs are web page URLs. Custom header information can be sent to the URL with the request to enable application-specific sessions.
- Changing the tab configuration of an app is done through the admin panel." --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path 10.wav
