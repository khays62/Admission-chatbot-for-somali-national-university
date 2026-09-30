# Qorshaha Dhismaha Admission Chatbot-ka SNU

## Ujeeddo
Doc-kan waxa uu qeexayaa sida loo dhisayo admission chatbot-ka Jaamacadda Ummadda Soomaaliyeed ka hor inta aan la bilaabin code-gareynta. Ujeeddadu ma aha in dib loo dhiso form-ka codsiga, balse in la sameeyo chatbot caawiye ah oo:
- ka jawaaba su'aalaha admission-ka
- user-ka siiya link-ga saxda ah ee form-ka live-ka ah marka uu doonayo isdiiwaan-gelin
- ka ilaaliya chatbot-ka inuu ka baxo mowduuca admission-ka
- si fudud ugu xirmi kara system-ka jira ee jaamacadda

## Go’aanka Aan Ku Heshinnay
Waxaan ku heshinnay in chatbot-ku uusan noqon form cusub. Wuxuu noqonayaa hagaha admission-ka oo leh laba shaqo oo waaweyn:
1. Inuu ka jawaabo su'aalaha ku saabsan admission-ka
2. Inuu qofka u gudbiyo form-ka live-ka ah marka uu rabo codsi rasmi ah

Taasi waa go’aan sax ah sababtoo ah form-ka live-ka ah hore ayuu u shaqaynayaa, sidaas darteed dib-u-dhis form cusub waxay noqonaysaa waqti lumis.

## Go’aannada Cusub Ee La Xaqiijiyey
Go’aannadan waxaa lagu go’aamiyey wada hadalka mashruuca:
1. Luqadda backend-ka waa Python.
2. Stack-ka la raacayo waa Flask + Jinja2.
3. PostgreSQL hadda lama dhisayo wajigan koowaad.
4. Kaydinta ku-meel-gaarka ah ee wajigan koowaad waa Session.
5. Local Storage waxaa loo isticmaali karaa ikhtiyaar labaad oo frontend ah haddii loo baahdo draft kooban.

Sababta Session loo doortay wajigan koowaad:
- xogta waxay ku xirmaysaa session-ka user-ka, waxayna ka ammaan badan tahay kaydinta joogtada ah ee browser-ka
- way fududahay in backend-ku xakameeyo nolosha xogta
- marka user-ku xiro session-ka ama waqtigu dhamaado, xogtu si dabiici ah ayey u dhammaanaysaa
- waxay ku habboon tahay prototype aan weli lahayn database production ah

Fiiro gaar ah: haddii mustaqbalka loo baahdo taariikh wada hadal, warbixin, ama analytics, PostgreSQL ayaa lagu dari karaa wajiga xiga.

## Waxa La Xaqiijiyey Ee Form-ka Live-ka Ah
Form-ka live-ka ah waxa uu muujinayaa in system-ku yahay server-rendered, isla markaana uu leeyahay:
- HTML
- CSS
- JavaScript
- jQuery
- Bootstrap 5.1.3
- Select2
- Font Awesome
- CSRF token
- form action ku socda endpoint-ka codsiga
- upload file ah oo ku socda `multipart/form-data`

Stack-ka backend-ka waxa uu si macquul ah ugu egyahay Flask + Jinja2 + PostgreSQL, balse database-ka si toos ah laguma xaqiijin karo browser-ka kaliya. Sidaa darteed, waxaan u qaadaneynaa in Flask/Jinja2/PostgreSQL ay yihiin doorashooyin ku habboon integration-ka, haddii kooxda system-ka hayaa ay sidaas hore ugu shaqaynayaan.

## Qaabka Guud Ee Chatbot-ka
Chatbot-ku waxa uu ku shaqaynayaa habkan:
1. Wuxuu salaamaa user-ka.
2. Wuxuu fahmaa waxa user-ku doonayo.
3. Haddii user-ku rabo codsi, wuxuu siiyaa link-ga rasmiga ah.
4. Haddii user-ku su'aal ka weydiiyo admission-ka, wuxuu ka jawaabaa knowledge base-ka.
5. Haddii su'aashu ka baxdo admission-ka, wuxuu user-ka ku celinayaa mowduuca saxda ah.
6. Haddii su'aashu u baahan tahay faahfaahin, wuxuu waydiinayaa su’aal ku xigta.

## Qaybaha Chatbot-ku Ka Kooban Yahay

### 1. Qaybta Jawaabaha Admission-ka
Qaybtan waxay ka jawaabaysaa:
- shuruudaha gelitaanka
- dokumentiyada loo baahan yahay
- lacag bixinta
- xarumaha iyo goobaha imtixaanka
- kuliyadaha la dooran karo
- xiriirka maamulka
- waqtiyada ama faahfaahinta muhiimka ah

### 2. Qaybta U Gudbinta Form-ka Live-ka Ah
Marka user-ku rabo inuu isdiiwaan geliyo, chatbot-ku si toos ah ayuu u siiyaa:
- link-ga form-ka live-ka ah
- tilmaamo kooban oo ku saabsan waxa uu u baahan yahay ka hor intuusan buuxin

### 3. Qaybta Mawduuca Ka Baxsan
Haddii user-ku ka baxo admission-ka, chatbot-ku waxa uu sameeyaa:
- digniin kooban
- celin mowduuca saxda ah
- haddii loo baahdo wuxuu siyaa doorashooyin admission-ka la xiriira

### 4. Qaybta Xogta Iyo Kaydinta
Haddii aan rabno in aan keydino wada hadalka ama xaaladda user-ka, waxaa la isticmaali karaa:
- session gudaha ah
- database
- local storage haddii uu yahay prototype fudud

## Qaabka Backend-ka Iyo Frontend-ka Loo Kala Qaybinayo

### Backend
Backend-ku waa inuu qabtaa waxyaabahan:
- aqoonsiga su'aasha user-ka
- soo saarista jawaabta saxda ah
- maamulka link-ga form-ka live-ka ah
- kaydinta session-ka ama conversation history-ga
- ilaalinta validation-ka iyo response logic-ka
- bixinta API-yada chatbot-ka

### Frontend
Frontend-ku waa inuu qabtaa waxyaabahan:
- chatbot UI
- input-ka user-ka
- rendering-ka jawaabaha
- show-gareynta suggestions-ka
- redirect button haddii user-ku rabo form-ka live-ka ah

### Kala Qaybinta Ugu Fiican
Si mashruucu u noqdo nadiif, waxaan kula talinayaa in backend iyo frontend la kala saaro. Haddii kooxda jaamacaddu hore u haysato Flask + Jinja2 system, chatbot-ka waxaa lagu dhex dari karaa sidii module gaar ah, balse logic-ga waa in uu weli ahaadaa modular.

## Requirements-ka Mashruuca

### Requirements-ka Functional
- User-ka waa inuu heli karaa jawaabo ku saabsan admission-ka
- User-ka waa inuu heli karaa link-ga codsiga live-ka ah
- Chatbot-ku waa inuu fahmaa intents-ka waaweyn
- Chatbot-ku waa inuu ka jawaabaa su'aalaha la oggol yahay
- Chatbot-ku waa inuu ka celin karaa su'aalaha aan la xiriirin admission-ka
- Chatbot-ku waa inuu taageeraa update fudud oo knowledge base ah

### Requirements-ka Non-Functional
- System-ku waa inuu fududaadaa in la ilaaliyo
- Response-ku waa inuu ahaadaa degdeg
- Code-ku waa inuu noqdaa modular
- Waxaa la rabaa in si fudud loogu xiro system-ka jira
- Waxaa fiican in uu noqdo responsive oo mobile-ka si fiican uga shaqeeya

## API-yada Aan U Baahanahay

### API-yada Muhiimka Ah
- `GET /api/admission-link`
- `GET /api/knowledge`
- `GET /api/faqs`
- `POST /api/chat/message`
- `POST /api/chat/intent`
- `POST /api/chat/redirect`

### API-yada Dheeraadka Ah Ee Session-ka
- `POST /api/chat/session/start`
- `GET /api/chat/session/state`
- `POST /api/chat/session/reset`

### API-yada Ikhtiyaariga Ah Ee Maamulka
- `POST /api/admin/faqs`
- `PUT /api/admin/faqs/:id`
- `DELETE /api/admin/faqs/:id`
- `POST /api/admin/knowledge`
- `PUT /api/admin/knowledge/:id`
- `GET /api/admin/conversations`

## Data Model-ka
Waxaa muhiim ah in xogta loo habeeyo qaybo cad cad:
- intents
- responses
- faq_items
- knowledge_items
- redirect_links
- conversation_sessions
- user_messages
- admin_notes

### Tusaale Qaybaha Knowledge Base-ka
- shuruudaha gelitaanka
- dokumentiyada loo baahan yahay
- lacagta codsiga
- kuliyadaha
- xarunta waxbarashada
- goobta imtixaanka
- contact info
- instructions-ka codsiga

## Folder Structure-ka La Taliyey

### Haddii Backend Iyo Frontend La Kala Qaybinayo
```text
frontend/
  src/
    components/
    pages/
    services/
    hooks/
    styles/
    utils/
  public/
  tests/

backend/
  src/
    routes/
    controllers/
    services/
    models/
    middleware/
    utils/
    config/
  tests/
  migrations/

docs/
  admission-chatbot-implementation-plan.md
  snu-admission-form-somali-spec.md
```

### Haddii Flask Lagu Dhisayo
```text
app/
  __init__.py
  config.py
  routes/
  services/
  models/
  templates/
  static/
  utils/
  data/
tests/
migrations/
docs/
```

## Logic-ka Chatbot-ka

### Intent-yada Ugu Muhiimsan
1. Salaan iyo soo dhaweyn
2. Su'aalaha admission-ka
3. Shuruudaha gelitaanka
4. Dokumentiyada loo baahan yahay
5. Lacag bixinta
6. Kuliyadaha
7. Xarunta iyo goobta imtixaanka
8. Codsi isdiiwaan-gelin
9. Su'aalo ka baxsan mowduuca

### Xeerarka Jawaabta
- Haddii user-ku rabo registration, link-ga rasmiga ah sii
- Haddii user-ku rabo sharaxaad, ka jawaab knowledge base-ka
- Haddii su'aashu aanay caddeyn, weydii su’aal caddayn ah
- Haddii su'aashu ka baxdo admission-ka, u celi mowduuca saxda ah
- Haddii xog cusub la helo, session-ka ku kaydi

### Siyaasadda API Model (GPT, Gemini, iwm)
Wajigan koowaad mashruucu API model dibadda ah ma qasbana. Tani ma aha diidmo joogto ah, waa go’aan wajiga koowaad ku habboon:
- kharashka wuu yaraadaa
- jawaabaha admission-ka waxay noqdaan kuwo xakameysan oo rasmi ah
- latency iyo ku-tiirsanaanta adeeg dibadeed way yaraadaan
- asturnaanta xogta user-ka way fududaataa in la ilaaliyo

Go’aanka saxda ah:
- hadda: rule-based intent + knowledge base
- mustaqbalka: model API waxaa loo dari karaa sidii lakab labaad oo caawinaya su'aalaha adag

## Sida Loo Adeegsado Form-ka Live-ka Ah Inuu Noqdo Knowledge Source
Waa macquul in form-ka live-ka ah laga dhigo source-ka ugu weyn ee knowledge base-ka, laakiin hab xakameysan:
1. Ha ku xirin scraping toos ah fariin kasta.
2. Ka soo saar field-yada iyo instructions-ka oo u rog JSON la xaqiijiyey.
3. Ku keydi nuqul version leh si isbeddellada loo maamulo.
4. Samee jadwal cusbooneysiin ah oo gacanta ama script leh.
5. Haddii docs iyo live form ay is-khilaafaan, live form ayaa mudnaan leh.

## Todolist Dhameystiran (La Cusboonaysiiyey)

### Wejiga 1: Diyaarinta Aasaaska (Hadda)
1. Xaqiiji scope-ka mashruuca: chatbot assistant, ma aha form cusub
2. Xaqiiji stack-ka wajiga koowaad: Python + Flask + Jinja2
3. Xaqiiji kaydinta wajiga koowaad: Session
4. Xaqiiji in PostgreSQL uu yahay wajiga xiga, ma aha hadda
5. Xaqiiji in API model (GPT/Gemini iwm) uu yahay wajiga xiga
6. Xaqiiji source-ka knowledge: live form mudnaan leh haddii khilaaf jiro
7. Qor liiska intents-ka ugu muhiimsan
8. Qor liiska response categories-ka
9. Qor liiska FAQ-ga koowaad
10. Qor policy-ga out-of-scope handling

### Wejiga 2: Qorshaha Farsamada
11. Go'aami API structure-ka final
12. Go'aami folder structure-ka final (backend/frontend kala go'an)
13. Qor contract-ka request/response ee endpoint walba
14. Qor session lifecycle (start, state, reset, expire)
15. Qor strategy-ga knowledge update (live form -> normalized JSON)

### Wejiga 3: Backend Development
16. Samee project skeleton-ka Flask
17. Samee config file-yada deegaanka
18. Samee routes-ka chatbot-ka
19. Samee intent router service
20. Samee FAQ matcher service
21. Samee redirect service ee live form
22. Samee session management
23. Samee validation iyo error handling
24. Samee test cases backend

### Wejiga 4: Frontend Development
25. Samee chatbot UI (qaab la jaanqaadaya style-ka portal-ka)
26. Samee input iyo message rendering
27. Samee loading states iyo fallback messages
28. Samee quick suggestion buttons
29. Samee redirect button ee form-ka live-ka ah
30. Samee mobile responsiveness
31. Samee frontend tests aasaasi ah

### Wejiga 5: Integration
32. Ku xiro frontend-ka backend-ka
33. Ku xiro knowledge base-ka API-ga
34. Ku xiro live form link-ga
35. Tijaabi intent response flow
36. Tijaabi out-of-scope handling
37. Tijaabi registration redirect

### Wejiga 6: Validation Iyo Hagaajin
38. Hubi in jawaabaha ay yihiin af-Soomaali nadiif ah
39. Hubi in policy-ga rasmi ah la raacayo
40. Hubi in live form had iyo jeer mudnaan leeyahay marka khilaaf jiro
41. Hubi in session expire logic sax yahay
42. Samee final review iyo release checklist

## Wejiga 1 Bilowga (Waxa Aan Hadda Isla Fulineyno)
Tani waa liiska shaqada ee bilowga degdegga ah:
1. Qeex dukumenti gaaban oo scope ah (hal bog)
2. Diyaari intents iyo response categories (version 1)
3. Diyaari FAQ-ga koowaad (10 ilaa 20 su'aalood)
4. Diyaari knowledge JSON koowaad oo ka tarjumaya live form-ka
5. Diyaari policy-ga out-of-scope response
6. Qeex admission live link response template

### Shuruudda Guusha Wejiga 1
Wejiga 1 wuxuu guuleystay marka:
- intents v1 la dhammeeyo
- faq v1 la dhammeeyo
- knowledge JSON v1 la dhammeeyo
- out-of-scope policy la ansixiyo
- redirect template la ansixiyo

## Waa Maxay Waxa Aan Hadda U Baahanahay Inaan Bilaabno?
Si mashruucu u dhaqaaqo, waxaan hadda u baahanahay 4 waxyaalood:
1. Qeexitaanka final-ka ah ee intent-yada
2. Knowledge base-ka kooban ee admission-ka
3. Tech stack-ka aan dooranayno
4. Qaabka folder structure-ka ugu dambeeya

## Go’aan Farsamo Oo La Taliyey
Haddii aad rabto qaab nadiif ah oo si fudud loogu xiro system-ka jaamacadda, waxaan kugula talinayaa:
- Backend: Flask
- Template layer: Jinja2 haddii loo baahdo
- Database: PostgreSQL
- Frontend: Bootstrap + JavaScript ama React haddii aad rabto UI casri ah
- Chat logic: rule-based intent router + FAQ matcher

Qaabkan wuxuu fududeynayaa in chatbot-ka lagu dhex daro system-ka jira, isla markaana aanu u baahnayn in la isticmaalo model AI dibadda ah hadda.

## Natiijada La Filayo
Marka mashruucu dhammaado, chatbot-ku waa inuu awoodaa:
- inuu si cad uga jawaabo admission questions
- inuu si sax ah u siiyo form link-ga live-ka ah
- inuu ka celiyo su'aalaha ka baxsan mowduuca
- inuu si nadiif ah ugu shaqeeyo frontend iyo backend kala go’an
- inuu noqdo mid si fudud loo cusboonaysiin karo mustaqbalka
