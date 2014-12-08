# Leo colorizer control file for tsql mode.
# This file is in the public domain.

# Properties for tsql mode.
properties = {
	"commentEnd": "*/",
	"commentStart": "/*",
	"lineComment": "--",
}

# Attributes dict for tsql_main ruleset.
tsql_main_attributes_dict = {
	"default": "null",
	"digit_re": "",
	"escape": "",
	"highlight_digits": "true",
	"ignore_case": "true",
	"no_word_sep": "",
}

# Dictionary of attributes dictionaries for tsql mode.
attributesDictDict = {
	"tsql_main": tsql_main_attributes_dict,
}

# Keywords dict for tsql_main ruleset.
tsql_main_keywords_dict = {
	"@@connections": "keyword2",
	"@@cpu_busy": "keyword2",
	"@@cursor_rows": "keyword2",
	"@@datefirst": "keyword2",
	"@@dbts": "keyword2",
	"@@error": "keyword2",
	"@@fetch_status": "keyword2",
	"@@identity": "keyword2",
	"@@idle": "keyword2",
	"@@io_busy": "keyword2",
	"@@langid": "keyword2",
	"@@language": "keyword2",
	"@@lock_timeout": "keyword2",
	"@@max_connections": "keyword2",
	"@@max_precision": "keyword2",
	"@@nestlevel": "keyword2",
	"@@options": "keyword2",
	"@@pack_received": "keyword2",
	"@@pack_sent": "keyword2",
	"@@packet_errors": "keyword2",
	"@@procid": "keyword2",
	"@@remserver": "keyword2",
	"@@rowcount": "keyword2",
	"@@servername": "keyword2",
	"@@servicename": "keyword2",
	"@@spid": "keyword2",
	"@@textsize": "keyword2",
	"@@timeticks": "keyword2",
	"@@total_errors": "keyword2",
	"@@total_read": "keyword2",
	"@@total_write": "keyword2",
	"@@trancount": "keyword2",
	"@@version": "keyword2",
	"abs": "keyword2",
	"absolute": "keyword1",
	"acos": "keyword2",
	"add": "keyword1",
	"all": "keyword1",
	"alter": "keyword1",
	"and": "keyword1",
	"ansi_nulls": "keyword1",
	"any": "keyword1",
	"app_name": "keyword2",
	"as": "keyword1",
	"asc": "keyword1",
	"ascii": "keyword2",
	"asin": "keyword2",
	"atan": "keyword2",
	"atn2": "keyword2",
	"authorization": "keyword1",
	"avg": "keyword2",
	"backup": "keyword1",
	"backupfile": "keyword3",
	"backupmediafamily": "keyword3",
	"backupmediaset": "keyword3",
	"backupset": "keyword3",
	"begin": "keyword1",
	"between": "keyword1",
	"binary": "keyword1",
	"binary_checksum": "keyword2",
	"bit": "keyword1",
	"break": "keyword1",
	"browse": "keyword1",
	"bulk": "keyword1",
	"by": "keyword1",
	"cascade": "keyword1",
	"case": "keyword2",
	"cast": "keyword2",
	"ceiling": "keyword2",
	"char": "keyword1",
	"character": "keyword1",
	"charindex": "keyword2",
	"check": "keyword1",
	"checkpoint": "keyword1",
	"checksum": "keyword2",
	"checksum_agg": "keyword2",
	"close": "keyword1",
	"clustered": "keyword1",
	"coalesce": "keyword2",
	"col_length": "keyword2",
	"col_name": "keyword2",
	"collationproperty": "keyword2",
	"column": "keyword1",
	"columnproperty": "keyword2",
	"commit": "keyword1",
	"committed": "keyword1",
	"compute": "keyword1",
	"confirm": "keyword1",
	"constraint": "keyword1",
	"contains": "keyword1",
	"containstable": "keyword1",
	"continue": "keyword1",
	"controlrow": "keyword1",
	"convert": "keyword2",
	"cos": "keyword2",
	"cot": "keyword2",
	"count": "keyword2",
	"count_big": "keyword2",
	"create": "keyword1",
	"cross": "keyword1",
	"current": "keyword1",
	"current_date": "keyword2",
	"current_time": "keyword2",
	"current_timestamp": "keyword2",
	"current_user": "keyword2",
	"cursor": "keyword1",
	"cursor_status": "keyword2",
	"database": "keyword1",
	"databaseproperty": "keyword2",
	"datalength": "keyword2",
	"dateadd": "keyword2",
	"datediff": "keyword2",
	"datename": "keyword2",
	"datepart": "keyword2",
	"datetime": "keyword1",
	"day": "keyword2",
	"db_id": "keyword2",
	"db_name": "keyword2",
	"dbcc": "keyword1",
	"deallocate": "keyword1",
	"decimal": "keyword1",
	"declare": "keyword1",
	"default": "keyword1",
	"degrees": "keyword2",
	"delete": "keyword1",
	"deny": "keyword1",
	"desc": "keyword1",
	"difference": "keyword2",
	"disk": "keyword1",
	"distinct": "keyword1",
	"distributed": "keyword1",
	"double": "keyword1",
	"drop": "keyword1",
	"dummy": "keyword1",
	"dump": "keyword1",
	"dynamic": "keyword1",
	"else": "keyword1",
	"end": "keyword1",
	"errlvl": "keyword1",
	"errorexit": "keyword1",
	"escape": "keyword1",
	"except": "keyword1",
	"exec": "keyword1",
	"execute": "keyword1",
	"exists": "keyword1",
	"exit": "keyword1",
	"exp": "keyword2",
	"fast_forward": "keyword1",
	"fetch": "keyword1",
	"file": "keyword1",
	"file_id": "keyword2",
	"file_name": "keyword2",
	"filegroup_id": "keyword2",
	"filegroup_name": "keyword2",
	"filegroupproperty": "keyword2",
	"fileproperty": "keyword2",
	"fillfactor": "keyword1",
	"first": "keyword1",
	"float": "keyword1",
	"floor": "keyword2",
	"floppy": "keyword1",
	"fn_helpcollations": "keyword3",
	"fn_servershareddrives": "keyword3",
	"fn_virtualfilestats": "keyword3",
	"for": "keyword1",
	"foreign": "keyword1",
	"formatmessage": "keyword2",
	"forward_only": "keyword1",
	"freetext": "keyword1",
	"freetexttable": "keyword1",
	"from": "keyword1",
	"full": "keyword1",
	"fulltextcatalogproperty": "keyword2",
	"fulltextserviceproperty": "keyword2",
	"function": "keyword1",
	"getansinull": "keyword2",
	"getdate": "keyword2",
	"getutcdate": "keyword2",
	"global": "keyword1",
	"goto": "keyword1",
	"grant": "keyword1",
	"group": "keyword1",
	"grouping": "keyword2",
	"having": "keyword1",
	"holdlock": "keyword1",
	"host_id": "keyword2",
	"host_name": "keyword2",
	"id": "keyword1",
	"ident_current": "keyword2",
	"ident_incr": "keyword2",
	"ident_seed": "keyword2",
	"identity": "keyword2",
	"identity_insert": "keyword2",
	"identitycol": "keyword1",
	"if": "keyword1",
	"image": "keyword1",
	"in": "keyword1",
	"index": "keyword1",
	"index_col": "keyword2",
	"indexproperty": "keyword2",
	"inner": "keyword1",
	"insensitive": "keyword1",
	"insert": "keyword1",
	"int": "keyword1",
	"integer": "keyword1",
	"intersect": "keyword1",
	"into": "keyword1",
	"is": "keyword1",
	"is_member": "keyword2",
	"is_srvrolemember": "keyword2",
	"isdate": "keyword2",
	"isnull": "keyword2",
	"isnumeric": "keyword2",
	"isolation": "keyword1",
	"join": "keyword1",
	"key": "keyword1",
	"keyset": "keyword1",
	"kill": "keyword1",
	"last": "keyword1",
	"left": "keyword2",
	"len": "keyword2",
	"level": "keyword1",
	"like": "keyword1",
	"lineno": "keyword1",
	"load": "keyword1",
	"local": "keyword1",
	"log": "keyword2",
	"log10": "keyword2",
	"lower": "keyword2",
	"ltrim": "keyword2",
	"max": "keyword1",
	"min": "keyword1",
	"mirrorexit": "keyword1",
	"money": "keyword1",
	"month": "keyword2",
	"msagent_parameters": "keyword3",
	"msagent_profiles": "keyword3",
	"msarticles": "keyword3",
	"msdistpublishers": "keyword3",
	"msdistribution_agents": "keyword3",
	"msdistribution_history": "keyword3",
	"msdistributiondbs": "keyword3",
	"msdistributor": "keyword3",
	"mslogreader_agents": "keyword3",
	"mslogreader_history": "keyword3",
	"msmerge_agents": "keyword3",
	"msmerge_contents": "keyword3",
	"msmerge_delete_conflicts": "keyword3",
	"msmerge_genhistory": "keyword3",
	"msmerge_history": "keyword3",
	"msmerge_replinfo": "keyword3",
	"msmerge_subscriptions": "keyword3",
	"msmerge_tombstone": "keyword3",
	"mspublication_access": "keyword3",
	"mspublications": "keyword3",
	"mspublisher_databases": "keyword3",
	"msrepl_commands": "keyword3",
	"msrepl_errors": "keyword3",
	"msrepl_originators": "keyword3",
	"msrepl_transactions": "keyword3",
	"msrepl_version": "keyword3",
	"msreplication_objects": "keyword3",
	"msreplication_subscriptions": "keyword3",
	"mssnapshot_agents": "keyword3",
	"mssnapshot_history": "keyword3",
	"mssubscriber_info": "keyword3",
	"mssubscriber_schedule": "keyword3",
	"mssubscription_properties": "keyword3",
	"mssubscriptions": "keyword3",
	"name": "keyword1",
	"national": "keyword1",
	"nchar": "keyword1",
	"newid": "keyword2",
	"next": "keyword1",
	"nocheck": "keyword1",
	"nonclustered": "keyword1",
	"not": "keyword1",
	"ntext": "keyword1",
	"null": "keyword1",
	"nullif": "keyword2",
	"numeric": "keyword1",
	"nvarchar": "keyword1",
	"object_id": "keyword2",
	"object_name": "keyword2",
	"objectproperty": "keyword2",
	"of": "keyword1",
	"off": "keyword1",
	"offsets": "keyword1",
	"on": "keyword1",
	"once": "keyword1",
	"only": "keyword1",
	"open": "keyword1",
	"opendatasource": "keyword1",
	"openquery": "keyword1",
	"openrowset": "keyword1",
	"optimistic": "keyword1",
	"option": "keyword1",
	"or": "keyword1",
	"order": "keyword1",
	"outer": "keyword1",
	"output": "keyword1",
	"over": "keyword1",
	"parsename": "keyword2",
	"patindex": "keyword2",
	"percent": "keyword1",
	"perm": "keyword1",
	"permanent": "keyword1",
	"permissions": "keyword2",
	"pi": "keyword2",
	"pipe": "keyword1",
	"plan": "keyword1",
	"power": "keyword2",
	"precision": "keyword1",
	"prepare": "keyword1",
	"primary": "keyword1",
	"print": "keyword1",
	"prior": "keyword1",
	"privileges": "keyword1",
	"proc": "keyword1",
	"procedure": "keyword1",
	"processexit": "keyword1",
	"public": "keyword1",
	"quoted_identifier": "keyword1",
	"quotename": "keyword2",
	"radians": "keyword2",
	"raiserror": "keyword1",
	"rand": "keyword2",
	"read": "keyword1",
	"read_only": "keyword1",
	"readtext": "keyword1",
	"real": "keyword1",
	"reconfigure": "keyword1",
	"references": "keyword1",
	"relative": "keyword1",
	"repeatable": "keyword1",
	"replace": "keyword2",
	"replicate": "keyword2",
	"replication": "keyword1",
	"restore": "keyword1",
	"restorefile": "keyword3",
	"restorefilegroup": "keyword3",
	"restorehistory": "keyword3",
	"restrict": "keyword1",
	"return": "keyword1",
	"returns": "keyword1",
	"reverse": "keyword2",
	"revoke": "keyword1",
	"right": "keyword2",
	"rollback": "keyword1",
	"round": "keyword2",
	"rowcount_big": "keyword2",
	"rowguidcol": "keyword1",
	"rtrim": "keyword2",
	"rule": "keyword1",
	"save": "keyword1",
	"schema": "keyword1",
	"scope_identity": "keyword2",
	"scroll": "keyword1",
	"scroll_locks": "keyword1",
	"select": "keyword1",
	"serializable": "keyword1",
	"serverproperty": "keyword2",
	"session_user": "keyword2",
	"sessionproperty": "keyword2",
	"set": "keyword1",
	"setuser": "keyword1",
	"shutdown": "keyword1",
	"sign": "keyword2",
	"sin": "keyword2",
	"smalldatetime": "keyword1",
	"smallint": "keyword1",
	"smallmoney": "keyword1",
	"some": "keyword1",
	"soundex": "keyword2",
	"sp_add_agent_parameter": "keyword3",
	"sp_add_agent_profile": "keyword3",
	"sp_add_alert": "keyword3",
	"sp_add_category": "keyword3",
	"sp_add_data_file_recover_suspect_db": "keyword3",
	"sp_add_job": "keyword3",
	"sp_add_jobschedule": "keyword3",
	"sp_add_jobserver": "keyword3",
	"sp_add_jobstep": "keyword3",
	"sp_add_log_file_recover_suspect_db": "keyword3",
	"sp_add_notification": "keyword3",
	"sp_add_operator": "keyword3",
	"sp_add_targetservergroup": "keyword3",
	"sp_add_targetsvrgrp_member": "keyword3",
	"sp_addalias": "keyword3",
	"sp_addapprole": "keyword3",
	"sp_addarticle": "keyword3",
	"sp_adddistpublisher": "keyword3",
	"sp_adddistributiondb": "keyword3",
	"sp_adddistributor": "keyword3",
	"sp_addextendedproc": "keyword3",
	"sp_addgroup": "keyword3",
	"sp_addlinkedserver": "keyword3",
	"sp_addlinkedsrvlogin": "keyword3",
	"sp_addlogin": "keyword3",
	"sp_addmergearticle": "keyword3",
	"sp_addmergefilter": "keyword3",
	"sp_addmergepublication": "keyword3",
	"sp_addmergepullsubscription": "keyword3",
	"sp_addmergepullsubscription_agent": "keyword3",
	"sp_addmergesubscription": "keyword3",
	"sp_addmessage": "keyword3",
	"sp_addpublication": "keyword3",
	"sp_addpublication_snapshot": "keyword3",
	"sp_addpublisher70": "keyword3",
	"sp_addpullsubscription": "keyword3",
	"sp_addpullsubscription_agent": "keyword3",
	"sp_addremotelogin": "keyword3",
	"sp_addrole": "keyword3",
	"sp_addrolemember": "keyword3",
	"sp_addserver": "keyword3",
	"sp_addsrvrolemember": "keyword3",
	"sp_addsubscriber": "keyword3",
	"sp_addsubscriber_schedule": "keyword3",
	"sp_addsubscription": "keyword3",
	"sp_addsynctriggers": "keyword3",
	"sp_addtabletocontents": "keyword3",
	"sp_addtask": "keyword3",
	"sp_addtype": "keyword3",
	"sp_addumpdevice": "keyword3",
	"sp_adduser": "keyword3",
	"sp_altermessage": "keyword3",
	"sp_apply_job_to_targets": "keyword3",
	"sp_approlepassword": "keyword3",
	"sp_article_validation": "keyword3",
	"sp_articlecolumn": "keyword3",
	"sp_articlefilter": "keyword3",
	"sp_articlesynctranprocs": "keyword3",
	"sp_articleview": "keyword3",
	"sp_attach_db": "keyword3",
	"sp_attach_single_file_db": "keyword3",
	"sp_autostats": "keyword3",
	"sp_bindefault": "keyword3",
	"sp_bindrule": "keyword3",
	"sp_bindsession": "keyword3",
	"sp_browsereplcmds": "keyword3",
	"sp_catalogs": "keyword3",
	"sp_certify_removable": "keyword3",
	"sp_change_agent_parameter": "keyword3",
	"sp_change_agent_profile": "keyword3",
	"sp_change_subscription_properties": "keyword3",
	"sp_change_users_login": "keyword3",
	"sp_changearticle": "keyword3",
	"sp_changedbowner": "keyword3",
	"sp_changedistpublisher": "keyword3",
	"sp_changedistributiondb": "keyword3",
	"sp_changedistributor_password": "keyword3",
	"sp_changedistributor_property": "keyword3",
	"sp_changegroup": "keyword3",
	"sp_changemergearticle": "keyword3",
	"sp_changemergefilter": "keyword3",
	"sp_changemergepublication": "keyword3",
	"sp_changemergepullsubscription": "keyword3",
	"sp_changemergesubscription": "keyword3",
	"sp_changeobjectowner": "keyword3",
	"sp_changepublication": "keyword3",
	"sp_changesubscriber": "keyword3",
	"sp_changesubscriber_schedule": "keyword3",
	"sp_changesubstatus": "keyword3",
	"sp_check_for_sync_trigger": "keyword3",
	"sp_column_privileges": "keyword3",
	"sp_column_privileges_ex": "keyword3",
	"sp_columns": "keyword3",
	"sp_columns_ex": "keyword3",
	"sp_configure": "keyword3",
	"sp_create_removable": "keyword3",
	"sp_createorphan": "keyword3",
	"sp_createstats": "keyword3",
	"sp_cursor": "keyword3",
	"sp_cursor_list": "keyword3",
	"sp_cursorclose": "keyword3",
	"sp_cursorexecute": "keyword3",
	"sp_cursorfetch": "keyword3",
	"sp_cursoropen": "keyword3",
	"sp_cursoroption": "keyword3",
	"sp_cursorprepare": "keyword3",
	"sp_cursorunprepare": "keyword3",
	"sp_cycle_errorlog": "keyword3",
	"sp_databases": "keyword3",
	"sp_datatype_info": "keyword3",
	"sp_dbcmptlevel": "keyword3",
	"sp_dbfixedrolepermission": "keyword3",
	"sp_dboption": "keyword3",
	"sp_defaultdb": "keyword3",
	"sp_defaultlanguage": "keyword3",
	"sp_delete_alert": "keyword3",
	"sp_delete_backuphistory": "keyword3",
	"sp_delete_category": "keyword3",
	"sp_delete_job": "keyword3",
	"sp_delete_jobschedule": "keyword3",
	"sp_delete_jobserver": "keyword3",
	"sp_delete_jobstep": "keyword3",
	"sp_delete_notification": "keyword3",
	"sp_delete_operator": "keyword3",
	"sp_delete_targetserver": "keyword3",
	"sp_delete_targetservergroup": "keyword3",
	"sp_delete_targetsvrgrp_member": "keyword3",
	"sp_deletemergeconflictrow": "keyword3",
	"sp_denylogin": "keyword3",
	"sp_depends": "keyword3",
	"sp_describe_cursor": "keyword3",
	"sp_describe_cursor_columns": "keyword3",
	"sp_describe_cursor_tables": "keyword3",
	"sp_detach_db": "keyword3",
	"sp_drop_agent_parameter": "keyword3",
	"sp_drop_agent_profile": "keyword3",
	"sp_dropalias": "keyword3",
	"sp_dropapprole": "keyword3",
	"sp_droparticle": "keyword3",
	"sp_dropdevice": "keyword3",
	"sp_dropdistpublisher": "keyword3",
	"sp_dropdistributiondb": "keyword3",
	"sp_dropdistributor": "keyword3",
	"sp_dropextendedproc": "keyword3",
	"sp_dropgroup": "keyword3",
	"sp_droplinkedsrvlogin": "keyword3",
	"sp_droplogin": "keyword3",
	"sp_dropmergearticle": "keyword3",
	"sp_dropmergefilter": "keyword3",
	"sp_dropmergepublication": "keyword3",
	"sp_dropmergepullsubscription": "keyword3",
	"sp_dropmergesubscription": "keyword3",
	"sp_dropmessage": "keyword3",
	"sp_droporphans": "keyword3",
	"sp_droppublication": "keyword3",
	"sp_droppullsubscription": "keyword3",
	"sp_dropremotelogin": "keyword3",
	"sp_droprole": "keyword3",
	"sp_droprolemember": "keyword3",
	"sp_dropserver": "keyword3",
	"sp_dropsrvrolemember": "keyword3",
	"sp_dropsubscriber": "keyword3",
	"sp_dropsubscription": "keyword3",
	"sp_droptask": "keyword3",
	"sp_droptype": "keyword3",
	"sp_dropuser": "keyword3",
	"sp_dropwebtask": "keyword3",
	"sp_dsninfo": "keyword3",
	"sp_dumpparamcmd": "keyword3",
	"sp_enumcodepages": "keyword3",
	"sp_enumcustomresolvers": "keyword3",
	"sp_enumdsn": "keyword3",
	"sp_enumfullsubscribers": "keyword3",
	"sp_execute": "keyword3",
	"sp_executesql": "keyword3",
	"sp_expired_subscription_cleanup": "keyword3",
	"sp_fkeys": "keyword3",
	"sp_foreignkeys": "keyword3",
	"sp_fulltext_catalog": "keyword3",
	"sp_fulltext_column": "keyword3",
	"sp_fulltext_database": "keyword3",
	"sp_fulltext_service": "keyword3",
	"sp_fulltext_table": "keyword3",
	"sp_generatefilters": "keyword3",
	"sp_get_distributor": "keyword3",
	"sp_getbindtoken": "keyword3",
	"sp_getmergedeletetype": "keyword3",
	"sp_grant_publication_access": "keyword3",
	"sp_grantdbaccess": "keyword3",
	"sp_grantlogin": "keyword3",
	"sp_help": "keyword3",
	"sp_help_agent_default": "keyword3",
	"sp_help_agent_parameter": "keyword3",
	"sp_help_agent_profile": "keyword3",
	"sp_help_alert": "keyword3",
	"sp_help_category": "keyword3",
	"sp_help_downloadlist": "keyword3",
	"sp_help_fulltext_catalogs": "keyword3",
	"sp_help_fulltext_catalogs_cursor": "keyword3",
	"sp_help_fulltext_columns": "keyword3",
	"sp_help_fulltext_columns_cursor": "keyword3",
	"sp_help_fulltext_tables": "keyword3",
	"sp_help_fulltext_tables_cursor": "keyword3",
	"sp_help_job": "keyword3",
	"sp_help_jobhistory": "keyword3",
	"sp_help_jobschedule": "keyword3",
	"sp_help_jobserver": "keyword3",
	"sp_help_jobstep": "keyword3",
	"sp_help_notification": "keyword3",
	"sp_help_operator": "keyword3",
	"sp_help_publication_access": "keyword3",
	"sp_help_targetserver": "keyword3",
	"sp_help_targetservergroup": "keyword3",
	"sp_helparticle": "keyword3",
	"sp_helparticlecolumns": "keyword3",
	"sp_helpconstraint": "keyword3",
	"sp_helpdb": "keyword3",
	"sp_helpdbfixedrole": "keyword3",
	"sp_helpdevice": "keyword3",
	"sp_helpdistpublisher": "keyword3",
	"sp_helpdistributiondb": "keyword3",
	"sp_helpdistributor": "keyword3",
	"sp_helpextendedproc": "keyword3",
	"sp_helpfile": "keyword3",
	"sp_helpfilegroup": "keyword3",
	"sp_helpgroup": "keyword3",
	"sp_helphistory": "keyword3",
	"sp_helpindex": "keyword3",
	"sp_helplanguage": "keyword3",
	"sp_helplinkedsrvlogin": "keyword3",
	"sp_helplogins": "keyword3",
	"sp_helpmergearticle": "keyword3",
	"sp_helpmergearticleconflicts": "keyword3",
	"sp_helpmergeconflictrows": "keyword3",
	"sp_helpmergedeleteconflictrows": "keyword3",
	"sp_helpmergefilter": "keyword3",
	"sp_helpmergepublication": "keyword3",
	"sp_helpmergepullsubscription": "keyword3",
	"sp_helpmergesubscription": "keyword3",
	"sp_helpntgroup": "keyword3",
	"sp_helppublication": "keyword3",
	"sp_helppullsubscription": "keyword3",
	"sp_helpremotelogin": "keyword3",
	"sp_helpreplicationdboption": "keyword3",
	"sp_helprole": "keyword3",
	"sp_helprolemember": "keyword3",
	"sp_helprotect": "keyword3",
	"sp_helpserver": "keyword3",
	"sp_helpsort": "keyword3",
	"sp_helpsrvrole": "keyword3",
	"sp_helpsrvrolemember": "keyword3",
	"sp_helpsubscriberinfo": "keyword3",
	"sp_helpsubscription": "keyword3",
	"sp_helpsubscription_properties": "keyword3",
	"sp_helptask": "keyword3",
	"sp_helptext": "keyword3",
	"sp_helptrigger": "keyword3",
	"sp_helpuser": "keyword3",
	"sp_indexes": "keyword3",
	"sp_indexoption": "keyword3",
	"sp_link_publication": "keyword3",
	"sp_linkedservers": "keyword3",
	"sp_lock": "keyword3",
	"sp_makewebtask": "keyword3",
	"sp_manage_jobs_by_login": "keyword3",
	"sp_mergedummyupdate": "keyword3",
	"sp_mergesubscription_cleanup": "keyword3",
	"sp_monitor": "keyword3",
	"sp_msx_defect": "keyword3",
	"sp_msx_enlist": "keyword3",
	"sp_oacreate": "keyword3",
	"sp_oadestroy": "keyword3",
	"sp_oageterrorinfo": "keyword3",
	"sp_oagetproperty": "keyword3",
	"sp_oamethod": "keyword3",
	"sp_oasetproperty": "keyword3",
	"sp_oastop": "keyword3",
	"sp_password": "keyword3",
	"sp_pkeys": "keyword3",
	"sp_post_msx_operation": "keyword3",
	"sp_prepare": "keyword3",
	"sp_primarykeys": "keyword3",
	"sp_processmail": "keyword3",
	"sp_procoption": "keyword3",
	"sp_publication_validation": "keyword3",
	"sp_purge_jobhistory": "keyword3",
	"sp_purgehistory": "keyword3",
	"sp_reassigntask": "keyword3",
	"sp_recompile": "keyword3",
	"sp_refreshsubscriptions": "keyword3",
	"sp_refreshview": "keyword3",
	"sp_reinitmergepullsubscription": "keyword3",
	"sp_reinitmergesubscription": "keyword3",
	"sp_reinitpullsubscription": "keyword3",
	"sp_reinitsubscription": "keyword3",
	"sp_remoteoption": "keyword3",
	"sp_remove_job_from_targets": "keyword3",
	"sp_removedbreplication": "keyword3",
	"sp_rename": "keyword3",
	"sp_renamedb": "keyword3",
	"sp_replcmds": "keyword3",
	"sp_replcounters": "keyword3",
	"sp_repldone": "keyword3",
	"sp_replflush": "keyword3",
	"sp_replication_agent_checkup": "keyword3",
	"sp_replicationdboption": "keyword3",
	"sp_replsetoriginator": "keyword3",
	"sp_replshowcmds": "keyword3",
	"sp_repltrans": "keyword3",
	"sp_reset_connection": "keyword3",
	"sp_resync_targetserver": "keyword3",
	"sp_revoke_publication_access": "keyword3",
	"sp_revokedbaccess": "keyword3",
	"sp_revokelogin": "keyword3",
	"sp_runwebtask": "keyword3",
	"sp_script_synctran_commands": "keyword3",
	"sp_scriptdelproc": "keyword3",
	"sp_scriptinsproc": "keyword3",
	"sp_scriptmappedupdproc": "keyword3",
	"sp_scriptupdproc": "keyword3",
	"sp_sdidebug": "keyword3",
	"sp_server_info": "keyword3",
	"sp_serveroption": "keyword3",
	"sp_setapprole": "keyword3",
	"sp_setnetname": "keyword3",
	"sp_spaceused": "keyword3",
	"sp_special_columns": "keyword3",
	"sp_sproc_columns": "keyword3",
	"sp_srvrolepermission": "keyword3",
	"sp_start_job": "keyword3",
	"sp_statistics": "keyword3",
	"sp_stop_job": "keyword3",
	"sp_stored_procedures": "keyword3",
	"sp_subscription_cleanup": "keyword3",
	"sp_table_privileges": "keyword3",
	"sp_table_privileges_ex": "keyword3",
	"sp_table_validation": "keyword3",
	"sp_tableoption": "keyword3",
	"sp_tables": "keyword3",
	"sp_tables_ex": "keyword3",
	"sp_unbindefault": "keyword3",
	"sp_unbindrule": "keyword3",
	"sp_unprepare": "keyword3",
	"sp_update_agent_profile": "keyword3",
	"sp_update_alert": "keyword3",
	"sp_update_category": "keyword3",
	"sp_update_job": "keyword3",
	"sp_update_jobschedule": "keyword3",
	"sp_update_jobstep": "keyword3",
	"sp_update_notification": "keyword3",
	"sp_update_operator": "keyword3",
	"sp_update_targetservergroup": "keyword3",
	"sp_updatestats": "keyword3",
	"sp_updatetask": "keyword3",
	"sp_validatelogins": "keyword3",
	"sp_validname": "keyword3",
	"sp_who": "keyword3",
	"space": "keyword2",
	"sqrt": "keyword2",
	"square": "keyword2",
	"static": "keyword1",
	"statistics": "keyword1",
	"stats_date": "keyword2",
	"stdev": "keyword2",
	"stdevp": "keyword2",
	"str": "keyword2",
	"stuff": "keyword2",
	"substring": "keyword2",
	"sum": "keyword2",
	"suser_id": "keyword2",
	"suser_name": "keyword2",
	"suser_sid": "keyword2",
	"suser_sname": "keyword2",
	"sysalerts": "keyword3",
	"sysallocations": "keyword3",
	"sysaltfiles": "keyword3",
	"sysarticles": "keyword3",
	"sysarticleupdates": "keyword3",
	"syscacheobjects": "keyword3",
	"syscategories": "keyword3",
	"syscharsets": "keyword3",
	"syscolumns": "keyword3",
	"syscomments": "keyword3",
	"sysconfigures": "keyword3",
	"sysconstraints": "keyword3",
	"syscurconfigs": "keyword3",
	"sysdatabases": "keyword3",
	"sysdepends": "keyword3",
	"sysdevices": "keyword3",
	"sysdownloadlist": "keyword3",
	"sysfilegroups": "keyword3",
	"sysfiles": "keyword3",
	"sysforeignkeys": "keyword3",
	"sysfulltextcatalogs": "keyword3",
	"sysindexes": "keyword3",
	"sysindexkeys": "keyword3",
	"sysjobhistory": "keyword3",
	"sysjobs": "keyword3",
	"sysjobschedules": "keyword3",
	"sysjobservers": "keyword3",
	"sysjobsteps": "keyword3",
	"syslanguages": "keyword3",
	"syslockinfo": "keyword3",
	"syslogins": "keyword3",
	"sysmembers": "keyword3",
	"sysmergearticles": "keyword3",
	"sysmergepublications": "keyword3",
	"sysmergeschemachange": "keyword3",
	"sysmergesubscriptions": "keyword3",
	"sysmergesubsetfilters": "keyword3",
	"sysmessages": "keyword3",
	"sysnotifications": "keyword3",
	"sysobjects": "keyword3",
	"sysoledbusers": "keyword3",
	"sysoperators": "keyword3",
	"sysperfinfo": "keyword3",
	"syspermissions": "keyword3",
	"sysprocesses": "keyword3",
	"sysprotects": "keyword3",
	"syspublications": "keyword3",
	"sysreferences": "keyword3",
	"sysremotelogins": "keyword3",
	"sysreplicationalerts": "keyword3",
	"sysservers": "keyword3",
	"syssubscriptions": "keyword3",
	"systargetservergroupmembers": "keyword3",
	"systargetservergroups": "keyword3",
	"systargetservers": "keyword3",
	"systaskids": "keyword3",
	"system_user": "keyword2",
	"systypes": "keyword3",
	"sysusers": "keyword3",
	"table": "keyword1",
	"tan": "keyword2",
	"tape": "keyword1",
	"temp": "keyword1",
	"temporary": "keyword1",
	"text": "keyword1",
	"textimage_on": "keyword1",
	"textptr": "keyword2",
	"textvalid": "keyword2",
	"then": "keyword1",
	"timestamp": "keyword1",
	"tinyint": "keyword1",
	"to": "keyword1",
	"top": "keyword1",
	"tran": "keyword1",
	"transaction": "keyword1",
	"trigger": "keyword1",
	"truncate": "keyword1",
	"tsequal": "keyword1",
	"typeproperty": "keyword2",
	"uncommitted": "keyword1",
	"unicode": "keyword2",
	"union": "keyword1",
	"unique": "keyword1",
	"uniqueidentifier": "keyword1",
	"update": "keyword1",
	"updatetext": "keyword1",
	"upper": "keyword2",
	"use": "keyword1",
	"user": "keyword2",
	"user_id": "keyword2",
	"user_name": "keyword2",
	"values": "keyword1",
	"var": "keyword2",
	"varbinary": "keyword1",
	"varchar": "keyword1",
	"varp": "keyword2",
	"varying": "keyword1",
	"view": "keyword1",
	"waitfor": "keyword1",
	"when": "keyword1",
	"where": "keyword1",
	"while": "keyword1",
	"with": "keyword1",
	"work": "keyword1",
	"writetext": "keyword1",
	"xp_cmdshell": "keyword3",
	"xp_deletemail": "keyword3",
	"xp_enumgroups": "keyword3",
	"xp_findnextmsg": "keyword3",
	"xp_grantlogin": "keyword3",
	"xp_logevent": "keyword3",
	"xp_loginconfig": "keyword3",
	"xp_logininfo": "keyword3",
	"xp_msver": "keyword3",
	"xp_readmail": "keyword3",
	"xp_revokelogin": "keyword3",
	"xp_sendmail": "keyword3",
	"xp_sprintf": "keyword3",
	"xp_sqlinventory": "keyword3",
	"xp_sqlmaint": "keyword3",
	"xp_sqltrace": "keyword3",
	"xp_sscanf": "keyword3",
	"xp_startmail": "keyword3",
	"xp_stopmail": "keyword3",
	"xp_trace_addnewqueue": "keyword3",
	"xp_trace_deletequeuedefinition": "keyword3",
	"xp_trace_destroyqueue": "keyword3",
	"xp_trace_enumqueuedefname": "keyword3",
	"xp_trace_enumqueuehandles": "keyword3",
	"xp_trace_eventclassrequired": "keyword3",
	"xp_trace_flushqueryhistory": "keyword3",
	"xp_trace_generate_event": "keyword3",
	"xp_trace_getappfilter": "keyword3",
	"xp_trace_getconnectionidfilter": "keyword3",
	"xp_trace_getcpufilter": "keyword3",
	"xp_trace_getdbidfilter": "keyword3",
	"xp_trace_getdurationfilter": "keyword3",
	"xp_trace_geteventfilter": "keyword3",
	"xp_trace_geteventnames": "keyword3",
	"xp_trace_getevents": "keyword3",
	"xp_trace_gethostfilter": "keyword3",
	"xp_trace_gethpidfilter": "keyword3",
	"xp_trace_getindidfilter": "keyword3",
	"xp_trace_getntdmfilter": "keyword3",
	"xp_trace_getntnmfilter": "keyword3",
	"xp_trace_getobjidfilter": "keyword3",
	"xp_trace_getqueueautostart": "keyword3",
	"xp_trace_getqueuedestination": "keyword3",
	"xp_trace_getqueueproperties": "keyword3",
	"xp_trace_getreadfilter": "keyword3",
	"xp_trace_getserverfilter": "keyword3",
	"xp_trace_getseverityfilter": "keyword3",
	"xp_trace_getspidfilter": "keyword3",
	"xp_trace_getsysobjectsfilter": "keyword3",
	"xp_trace_gettextfilter": "keyword3",
	"xp_trace_getuserfilter": "keyword3",
	"xp_trace_getwritefilter": "keyword3",
	"xp_trace_loadqueuedefinition": "keyword3",
	"xp_trace_pausequeue": "keyword3",
	"xp_trace_restartqueue": "keyword3",
	"xp_trace_savequeuedefinition": "keyword3",
	"xp_trace_setappfilter": "keyword3",
	"xp_trace_setconnectionidfilter": "keyword3",
	"xp_trace_setcpufilter": "keyword3",
	"xp_trace_setdbidfilter": "keyword3",
	"xp_trace_setdurationfilter": "keyword3",
	"xp_trace_seteventclassrequired": "keyword3",
	"xp_trace_seteventfilter": "keyword3",
	"xp_trace_sethostfilter": "keyword3",
	"xp_trace_sethpidfilter": "keyword3",
	"xp_trace_setindidfilter": "keyword3",
	"xp_trace_setntdmfilter": "keyword3",
	"xp_trace_setntnmfilter": "keyword3",
	"xp_trace_setobjidfilter": "keyword3",
	"xp_trace_setqueryhistory": "keyword3",
	"xp_trace_setqueueautostart": "keyword3",
	"xp_trace_setqueuecreateinfo": "keyword3",
	"xp_trace_setqueuedestination": "keyword3",
	"xp_trace_setreadfilter": "keyword3",
	"xp_trace_setserverfilter": "keyword3",
	"xp_trace_setseverityfilter": "keyword3",
	"xp_trace_setspidfilter": "keyword3",
	"xp_trace_setsysobjectsfilter": "keyword3",
	"xp_trace_settextfilter": "keyword3",
	"xp_trace_setuserfilter": "keyword3",
	"xp_trace_setwritefilter": "keyword3",
	"year": "keyword2",
}

# Dictionary of keywords dictionaries for tsql mode.
keywordsDictDict = {
	"tsql_main": tsql_main_keywords_dict,
}

# Rules for tsql_main ruleset.

def tsql_rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def tsql_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def tsql_rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def tsql_rule3(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="[", end="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def tsql_rule4(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def tsql_rule5(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="--",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def tsql_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!>",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="::",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def tsql_rule22(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def tsql_rule23(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal2", pattern="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def tsql_rule24(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for tsql_main ruleset.
rulesDict1 = {
	"!": [tsql_rule18,tsql_rule19,tsql_rule20,],
	"\"": [tsql_rule1,],
	"%": [tsql_rule13,],
	"&": [tsql_rule14,],
	"'": [tsql_rule2,],
	"(": [tsql_rule4,],
	"*": [tsql_rule9,],
	"+": [tsql_rule6,],
	"-": [tsql_rule5,tsql_rule7,],
	"/": [tsql_rule0,tsql_rule8,],
	"0": [tsql_rule24,],
	"1": [tsql_rule24,],
	"2": [tsql_rule24,],
	"3": [tsql_rule24,],
	"4": [tsql_rule24,],
	"5": [tsql_rule24,],
	"6": [tsql_rule24,],
	"7": [tsql_rule24,],
	"8": [tsql_rule24,],
	"9": [tsql_rule24,],
	":": [tsql_rule21,tsql_rule22,],
	"<": [tsql_rule12,],
	"=": [tsql_rule10,],
	">": [tsql_rule11,],
	"@": [tsql_rule23,tsql_rule24,],
	"A": [tsql_rule24,],
	"B": [tsql_rule24,],
	"C": [tsql_rule24,],
	"D": [tsql_rule24,],
	"E": [tsql_rule24,],
	"F": [tsql_rule24,],
	"G": [tsql_rule24,],
	"H": [tsql_rule24,],
	"I": [tsql_rule24,],
	"J": [tsql_rule24,],
	"K": [tsql_rule24,],
	"L": [tsql_rule24,],
	"M": [tsql_rule24,],
	"N": [tsql_rule24,],
	"O": [tsql_rule24,],
	"P": [tsql_rule24,],
	"Q": [tsql_rule24,],
	"R": [tsql_rule24,],
	"S": [tsql_rule24,],
	"T": [tsql_rule24,],
	"U": [tsql_rule24,],
	"V": [tsql_rule24,],
	"W": [tsql_rule24,],
	"X": [tsql_rule24,],
	"Y": [tsql_rule24,],
	"Z": [tsql_rule24,],
	"[": [tsql_rule3,],
	"^": [tsql_rule16,],
	"_": [tsql_rule24,],
	"a": [tsql_rule24,],
	"b": [tsql_rule24,],
	"c": [tsql_rule24,],
	"d": [tsql_rule24,],
	"e": [tsql_rule24,],
	"f": [tsql_rule24,],
	"g": [tsql_rule24,],
	"h": [tsql_rule24,],
	"i": [tsql_rule24,],
	"j": [tsql_rule24,],
	"k": [tsql_rule24,],
	"l": [tsql_rule24,],
	"m": [tsql_rule24,],
	"n": [tsql_rule24,],
	"o": [tsql_rule24,],
	"p": [tsql_rule24,],
	"q": [tsql_rule24,],
	"r": [tsql_rule24,],
	"s": [tsql_rule24,],
	"t": [tsql_rule24,],
	"u": [tsql_rule24,],
	"v": [tsql_rule24,],
	"w": [tsql_rule24,],
	"x": [tsql_rule24,],
	"y": [tsql_rule24,],
	"z": [tsql_rule24,],
	"|": [tsql_rule15,],
	"~": [tsql_rule17,],
}

# x.rulesDictDict for tsql mode.
rulesDictDict = {
	"tsql_main": rulesDict1,
}

# Import dict for tsql mode.
importDict = {}

