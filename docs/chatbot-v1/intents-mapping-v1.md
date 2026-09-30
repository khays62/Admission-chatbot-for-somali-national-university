# Intents Mapping V1

Ujeeddo: Qeexitaanka maagaan leh ee intent kasta, weedho-tusaale, iyo mapping-ka response-ka.

## Intent 1: salaam
- **Magaca Intent:** salaam
- **Weedho Tusaale:**
  - "As-salaam alaikum"
  - "Ku soo dhawoow"
  - "Hello"
  - "Hi"
- **Nooca Response:** greeting_welcome
- **Response:** "Ku soo dhawoow! Waxaan kaa caawin karaa su'aalaha admission-ka, shuruudaha, dokumentiyada, ama waxyaalaha kale ee codsiga jaamacadda."
- **Talaabo Xigta:** Weydii user-ka waxa uu doonayo

## Intent 2: codsi_isdiiwaan_gelin
- **Magaca Intent:** codsi_isdiiwaan_gelin
- **Weedho Tusaale:**
  - "Waan isdiiwaan gelinayaa"
  - "Waxaan raba inaan codsi buuxiyo"
  - "I want to apply"
  - "How do I register"
- **Nooca Response:** redirect_to_live_form
- **Response:** "Waxaad ka bilaabi kartaa bogga codsiga rasmiga ah: https://student.snu.edu.so/admission/online-application\n\nKahor intaad bilowdo, hubi in aad iskaan (scan) ama sawir ku heysato: sawir arday, aqoonsi, shahaado, iyo rasiidka bangiga."
- **Talaabo Xigta:** Qadan session "application_started"

## Intent 3: shuruudo_gelitaan
- **Magaca Intent:** shuruudo_gelitaan
- **Weedho Tusaale:**
  - "Maxaa shuruudaha?"
  - "Sidee ay u kala duwanaan yihiin shuruudaha?"
  - "What are requirements?"
- **Nooca Response:** faq_requirements
- **Response:** "Shuruudaha gelitaanka ay ku badiyaan kula xiriira dhashada, waxbarasho, iyo natiijada imtixaanka. Waxaa main ah in aad lahayd shaahaado dugsiga sare ama imtixaan certificate ah."
- **Talaabo Xigta:** Weydii su'aal xigta

## Intent 4: dukumentiyo_loo_baahan_yahay
- **Magaca Intent:** dukumentiyo_loo_baahan_yahay
- **Weedho Tusaale:**
  - "Maxaa dokumenti?"
  - "Documenti waa maxay?"
  - "What files do I need?"
- **Nooca Response:** faq_documents
- **Response:** "Waxaa la rabaa:\n1. Sawir arday (PNG/JPG - max 5MB)\n2. Aqoonsi NIRA/Passport/Dhalasho\n3. Shahaado dugsiga sare ama exam ID\n4. Rasiidka bangiga ee lacag bixinta\n\nWaxyaalaha 2-4 waxay qabtaan PDF/JPG/PNG - ugu badan 10MB mid walba."
- **Talaabo Xigta:** Weydii waxaa kale oo loo baahdo

## Intent 5: lacag_bixin_codsi
- **Magaca Intent:** lacag_bixin_codsi
- **Weedho Tusaale:**
  - "Lacagta codsiga goorma ayaan bixiyaa?"
  - "Bangiga maxaad dooro?"
  - "When do I pay?"
- **Nooca Response:** faq_payment
- **Response:** "Lacagta codsiga waa in la dhammeeyaa ka hor gudbinta codsiga. Waxaad dooran kartaa mid ka mid ah: Premier Bank, Salaam Bank, Dahabshiil Bank, IBS Bank, ama Amal Bank.\n\nMarka uu la bixiyay, hubi in aad heysato rasiidka iyo tixraaca bangiga si aad uga xaseexo codsiga."
- **Talaabo Xigta:** Weydii su'aal kale

## Intent 6: kuliyado_doorasho
- **Magaca Intent:** kuliyado_doorasho
- **Weedho Tusaale:**
  - "Kuliyado maxay yihiin?"
  - "Sida ku dooran karaa kuliyad?"
  - "What faculties are available?"
- **Nooca Response:** faq_faculties
- **Response:** "Waxaad dooran kartaa ilaa 3 kuliyad. Kuliyado waxay ka mid tahay:\n- Faculty of Engineering\n- Faculty of Medicine and Surgery\n- Faculty of Law\n- Faculty of Education\n- Faculty of Science\n- Faculty of Agriculture\n...iyo kale. Midka ugu wanaagsanaa hore dooro."
- **Talaabo Xigta:** Weydii wax kale

## Intent 7: xarun_iyo_goob_imtixaan
- **Magaca Intent:** xarun_iyo_goob_imtixaan
- **Weedho Tusaale:**
  - "Xaruna maxay yihiin?"
  - "Goobta imtixaanka waa maxay?"
  - "Where will I take the exam?"
- **Nooca Response:** faq_campus_location
- **Response:** "Xarumaha waxbarashada ay ka mid yihiin: Shabelle, Gahayr, Km4, Abudwaq, ama Badhan.\n\nGoobta imtixaanka waxaad dooran kartaa: Gahayr, Km4, Abudwaq, Badhan, Baydhabo, Garowe, ama Baladwayne."
- **Talaabo Xigta:** Weydii su'aal xigta

## Intent 8: sida_foomka_loobuuxiyo
- **Magaca Intent:** sida_foomka_loobuuxiyo
- **Weedho Tusaale:**
  - "Sidee aya foomka loo buuxiyo?"
  - "How do I fill the form?"
- **Nooca Response:** redirect_to_live_form
- **Response:** "Foomka waxa uu ka kooban yahay 4 qaybood: Personal Info, Academic, Documents, Review & Submit. Waxaad hal qaybood halkii kala shaqeeyn kartaa.\n\nHubi in aad buuxisay meelaha marked ah * kahor intaad gudbisho."
- **Talaabo Xigta:** Redirect bogga live form

## Intent 9: xiriir_iyo_taageero
- **Magaca Intent:** xiriir_iyo_taageero
- **Weedho Tusaale:**
  - "Sidee iska xiraan?"
  - "Contact info?"
  - "How do I reach support?"
- **Nooca Response:** contact_info
- **Response:** "Xiriiriyeyaal maamulka:\n📞 +252 866002 / 866003 / 866004\n📧 Jus@snu.edu.so\n🕐 Mon-Fri: 8:00 AM - 5:00 PM\n📍 Jidka Columbia, Xamar Weyne, Muqdisho"
- **Talaabo Xigta:** End chat ama weydii wax kale

## Intent 10: su_aal_aan_caddayn
- **Magaca Intent:** su_aal_aan_caddayn
- **Weedho Tusaale:**
  - "Waxaan is fahmin karin"
  - "Mahadsanid"
  - "I don't understand"
- **Nooca Response:** ask_clarification
- **Response:** "Fadlan su'aashaada si cad u sheeg ama dooro mid ka mid ah kuwan:\n- Codsiga\n- Shuruudaha\n- Dokumentiyada\n- Lacag bixinta\n- Kuliyadaha\n- Xarumaha"
- **Talaabo Xigta:** Weydii su'aal cad

## Intent 11: ka_baxsan_mowduuca
- **Magaca Intent:** ka_baxsan_mowduuca
- **Weedho Tusaale:**
  - "Maxaa waxaa kale?"
  - "Something else"
  - "Not related to admission"
- **Nooca Response:** out_of_scope
- **Response:** "Waxaan ku takhasusay su'aalaha admission-ka jaamacadda. Ma rabtaa inaan kaa caawiyo shuruudaha gelitaanka, dokumentiyada, ama link-ga codsiga rasmiga ah?"
- **Talaabo Xigta:** Weydii doorasho admission-ka

