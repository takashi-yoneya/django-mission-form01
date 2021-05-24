﻿# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from datetime import datetime as dt
from datetime import timedelta as delta
from sqlalchemy import Column, String,Text ,DateTime, Float, Integer, ForeignKey, Boolean, func, update
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.sql.type_api import STRINGTYPE
from sqlalchemy_utils import UUIDType
from pytz import timezone

from common.database import Base, get_ulid, session
from common.logger import set_logger
from common.utility import now_timestamp


class FetchUrl(Base):
    __tablename__ = 't_fetch_url'
    mysql_charset = 'utf8mb4',
    mysql_collate = 'utf8mb4_unicode_ci'

    id = Column('id', Integer, primary_key=True)
    account_id = Column('account_id', String(100), nullable=False)
    url = Column('url', String(64), nullable=False)
    is_completed = Column('is_completed', Boolean, default=False)
    created_at = Column('created_at', DateTime, nullable=False,
                        server_default=current_timestamp())
    updated_at = Column('updated_at', DateTime, nullable=False,
                        default=current_timestamp(), onupdate=func.utc_timestamp())
