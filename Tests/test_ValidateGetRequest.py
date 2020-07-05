import pytest
import configparser
import logging
import sys
from Tests.Helper import httpRequests
#from Tests.Helper.logger import SetupLogger
from Tests.Helper import utils
import warnings
warnings.filterwarnings("ignore")

#SetupLogger.initialize('Get_MarvelData')
logging.basicConfig(level=logging.INFO, file='MarvelTest.log')

try:
    cfg = configparser.ConfigParser()
    cfg.read('Helper/shared.constants.ini')
except:
    logging.error('Unable to read config file')
    sys.exit(1)

def test_charctersListWithDescription(setup):
    url = cfg.get('MarvelDataValidation','url')
    response = httpRequests.makeGetRequest(url,False)
    assert response.status_code == 200,'Status code for Get request is not 200'
    main_body = utils.getDataFromJson(response, 'data.results')
    characters = descriptions = series = []
    for i in range(len(main_body)):
        description = utils.getDataFromJson(response,'data.results.' + str(i)+'.description')
        character = utils.getDataFromJson(response,'data.results.' + str(i)+'.name')
        if(len(description)>0):
            characters.append(character)
            descriptions.append(description)
            series.append(utils.getDataFromJson(response,'data.results.' + str(i)+'.series'))
    logging.info("test passed")
    print(tuple(zip(characters,descriptions,series)))


def test_storiesWithoutCharacterDescription(setup):
    url = cfg.get('MarvelDataValidation','url')
    response = httpRequests.makeGetRequest(url,False)
    assert response.status_code == 200,'Status code for Get request is not 200'
    main_body = utils.getDataFromJson(response,'data.results')
    characters = stories = []
    for i in range(len(main_body)):
        description = utils.getDataFromJson(response,'data.results.' + str(i)+'.description')
        character = utils.getDataFromJson(response,'data.results.' + str(i)+'.name')
        if(len(description)==0):
            characters.append(character)
            stories.append(utils.getDataFromJson(response,'data.results.' + str(i)+'.stories'))
    print(tuple(zip(characters,stories)))








