from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order

countries = ['Select Country', 
			"Afghanistan",
			"Åland Islands",
			"Albania",
			"Algeria",
			"American Samoa",
			"Andorra",
			"Angola",
			"Anguilla",
			"Antarctica",
			"Antigua and Barbuda",
			"Argentina",
			"Armenia",
			"Aruba",
			"Australia",
			"Austria",
			"Azerbaijan",
			"Bahamas",
			"Bahrain",
			"Bangladesh",
			"Barbados",
			"Belarus",
			"Belgium",
			"Belize",
			"Benin",
			"Bermuda",
			"Bhutan",
			"Bolivia",
			"Bosnia and Herzegovina",
			"Botswana",
			"Bouvet Island",
			"Brazil",
			"British Indian Ocean Territory",
			"Brunei Darussalam",
			"Bulgaria",
			"Burkina Faso",
			"Burundi",
			"Cambodia",
			"Cameroon",
			"Canada",
			"Cape Verde",
			"Cayman Islands",
			"Central African Republic",
			"Chad",
			"Chile",
			"China",
			"Christmas Island",
			"Cocos (Keeling) Islands",
			"Colombia",
			"Comoros",
			"Congo",
			"Congo, The Democratic Republic of The",
			"Cook Islands",
			"Costa Rica",
			"Cote D'ivoire",
			"Croatia",
			"Cuba",
			"Cyprus",
			"Czech Republic",
			"Denmark",
			"Djibouti",
			"Dominica",
			"Dominican Republic",
			"Ecuador",
			"Egypt",
			"El Salvador",
			"Equatorial Guinea",
			"Eritrea",
			"Estonia",
			"Ethiopia",
			"Faroe Islands",
			"Fiji",
			"Finland",
			"France",
			"French Guiana",
			"French Polynesia",
			"French Southern Territories",
			"Gabon",
			"Gambia",
			"Georgia",
			"Germany",
			"Ghana",
			"Gibraltar",
			"Greece",
			"Greenland",
			"Grenada",
			"Guadeloupe",
			"Guam",
			"Guatemala",
			"Guernsey",
			"Guinea",
			"Guinea-bissau",
			"Guyana",
			"Haiti",
			"Heard Island and Mcdonald Islands",
			"Honduras",
			"Hong Kong",
			"Hungary",
			"Iceland",
			"India",
			"Indonesia",
			"Iran, Islamic Republic of",
			"Iraq",
			"Ireland",
			"Isle of Man",
			"Israel",
			"Italy",
			"Jamaica",
			"Japan",
			"Jersey",
			"Jordan",
			"Kazakhstan",
			"Kenya",
			"Kiribati",
			"Korea, Democratic People's Republic of",
			"Korea, Republic of",
			"Kuwait",
			"Kyrgyzstan",
			"Lao People's Democratic Republic",
			"Latvia",
			"Lebanon",
			"Lesotho",
			"Liberia",
			"Libyan Arab Jamahiriya",
			"Liechtenstein",
			"Lithuania",
			"Luxembourg",
			"Macao",
			"Macedonia, The Former Yugoslav Republic of",
			"Madagascar",
			"Malawi",
			"Malaysia",
			"Maldives",
			"Mali",
			"Malta",
			"Marshall Islands",
			"Martinique",
			"Mauritania",
			"Mauritius",
			"Mayotte",
			"Mexico",
			"Micronesia, Federated States of",
			"Moldova, Republic of",
			"Monaco",
			"Mongolia",
			"Montenegro",
			"Montserrat",
			"Morocco",
			"Mozambique",
			"Myanmar",
			"Namibia",
			"Nauru",
			"Nepal",
			"Netherlands",
			"Netherlands Antilles",
			"New Caledonia",
			"New Zealand",
			"Nicaragua",
			"Niger",
			"Nigeria",
			"Niue",
			"Norfolk Island",
			"Northern Mariana Islands",
			"Norway",
			"Oman",
			"Pakistan",
			"Palau",
			"Palestinian Territory, Occupied",
			"Panama",
			"Papua New Guinea",
			"Paraguay",
			"Peru",
			"Philippines",
			"Pitcairn",
			"Poland",
			"Portugal",
			"Puerto Rico",
			"Qatar",
			"Reunion",
			"Romania",
			"Russian Federation",
			"Rwanda",
			"Saint Helena",
			"Saint Kitts and Nevis",
			"Saint Lucia",
			"Saint Pierre and Miquelon",
			"Saint Vincent and The Grenadines",
			"Samoa",
			"San Marino",
			"Sao Tome and Principe",
			"Saudi Arabia",
			"Senegal",
			"Serbia",
			"Seychelles",
			"Sierra Leone",
			"Singapore",
			"Slovakia",
			"Slovenia",
			"Solomon Islands",
			"Somalia",
			"South Africa",
			"South Georgia and The South Sandwich Islands",
			"Spain",
			"Sri Lanka",
			"Sudan",
			"Suriname",
			"Svalbard and Jan Mayen",
			"Swaziland",
			"Sweden",
			"Switzerland",
			"Syrian Arab Republic",
			"Taiwan, Province of China",
			"Tajikistan",
			"Tanzania, United Republic of",
			"Thailand",
			"Timor-leste",
			"Togo",
			"Tokelau",
			"Tonga",
			"Trinidad and Tobago",
			"Tunisia",
			"Turkey",
			"Turkmenistan",
			"Turks and Caicos Islands",
			"Tuvalu",
			"Uganda",
			"Ukraine",
			"United Arab Emirates",
			"United Kingdom",
			"United States",
			"United States Minor Outlying Islands",
			"Uruguay",
			"Uzbekistan",
			"Vanuatu",
			"Venezuela",
			"Viet Nam",
			"Virgin Islands, British",
			"Wallis and Futuna",
			"Western Sahara",
			"Yemen",
			"Zambia",
			"Zimbabwe",

]

COUNTRY_CHOICES = [(i, i ) for i in countries]

# form for users to fill and place orders
class OrderCreateForm(forms.ModelForm):
	# postal_code = USZipCodeField()
	class Meta:
		model = Order
		fields = ['first_name', 'last_name',
					'email', 'address', 'city',
					'country', 'postal_code', 
					'phone', ]
		labels = {
			'first_name': '', 
			'last_name': '',
			'email': '',
			'address': '',
			'city': '',
			'country': '',
			'postal_code': '', 
			'phone': '',
		}
		widgets = {
            'first_name': forms.TextInput(

				attrs={'label': '',
					'type':  'text',
					'class': 'input',
					'placeholder': 'First Name',
					'name': 'first_name',
					}
				),
            'last_name': forms.TextInput(
				attrs={
					'type':  'text',
					'class': 'input',
					'placeholder': 'Last Name',
					'name': 'last_name',
					}
				),
            'email': forms.EmailInput(
				attrs={
					'type':  'email',
					'class': 'input',
					'class': 'input',
					'placeholder': 'Email'
					}
				),
             'address': forms.TextInput(
				attrs={
					'type':  'text',
					'class': 'input',
					'placeholder': 'Address',
					'name': 'address',
					}
				),
             'city': forms.TextInput(
				attrs={
					'type':  'text',
					'class': 'input',
					'placeholder': 'City',
					'name': 'city',
					}
				),
             'country': forms.Select(
             	choices = COUNTRY_CHOICES,
				attrs={
					'type':  'text',
					'class': 'input',
					'placeholder': 'Country',
					'name': 'country',
					}
				),
             'postal_code': forms.TextInput(
				attrs={
					'type':  'text',
					'class': 'input',
					'placeholder': 'Postal Code',
					'name': 'postal_code',
					}
				),
             'phone': forms.NumberInput(
				attrs={
					'type':  'tel',
					'class': 'input',
					'placeholder': 'Telephone',
					'name': 'phone',
					}
				),
		}

