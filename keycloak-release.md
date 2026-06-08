区分,対象リソース/データソース,変更タイプ,変更概要,詳細 & 対応アクション
プロバイダ,全般 / プロバイダ,バリデーション強化,リソースのインポート形式に関するバリデーションが強化されました。,プロバイダ全体で、不完全な形式のインポート入力に対して誤って正常と判定してしまう不具合が修正されました。今後、'terraform import' に指定するすべての GCP リソース ID は、ドキュメントに指定されたインポート形式に正確に一致する必要があります。
データソース,google_service_account_key,フィールド削除,project フィールドが削除されました。,project フィールドが削除されました。既存の設定ファイルから安全に削除してください。
リソース,google_alloydb_cluster,動作変更（削除保護）,deletion_protection によるクラスター削除保護がデフォルトで有効になりました。,deletion_protection フィールドが追加され、デフォルト値が true に設定されました。これにより、terraform apply 実行中の意図しないクラスターの破壊や再作成が防止されます。バージョン 7.0.0 では、設定で明示的にオフにしていない限り、次回のリフレッシュ時に既存のクラスターの削除保護も自動的に true に設定されます。
リソース,google_apigee_keystores_aliases_key_cert_file,フレームワーク移行 / フィールド変更,Plugin Framework への移行、および certs_info が参照専用（output-only）に変更されました。,SDKv2 からモダンな Plugin Framework に移行されました。以前は certs_info が任意指定可能でしたが、API で使用されていなかったため参照専用に修正されました。設定に記述されている場合は削除してください（API から取得された値は引き続き利用可能です）。
リソース,google_artifact_registry_repository,デフォルト値削除,public_repository 各フィールドのデフォルト値が削除されました。,public_repository フィールドのデフォルト値が削除されました。以前のデフォルト動作に依存していた場合は、手動で設定ファイルに記述を追加する必要があります。
リソース,google_beyondcorp_application,リソース削除,リソース本体および関連する IAM リソースが削除されました。,google_beyondcorp_application、関連する IAM リソース（_iam_binding、_iam_member、_iam_policy）、および _iam_policy データソースが削除されました。今後は google_beyondcorp_security_gateway_application を使用してください。
リソース,google_bigquery_table,デフォルト値削除,view.use_legacy_sql のデフォルト値（True）が削除されました。,デフォルト値が削除されました。既存のビューには影響ありませんが、新規にビューを作成する際にこのフィールドを未指定にすると、API側のデフォルトに従って legacy SQL として作成されます。
リソース,google_bigtable_table_iam_binding,フィールド削除（移行）,instance フィールドが削除され、instance_name に統合されました。,instance フィールドが削除され、instance_name に変更されました。v7.0.0+ にアップグレードする前に、v6.50.0+ にアップグレードした上で設定ファイルを instance_name に書き換えておくことが推奨されます。
リソース,google_bigtable_table_iam_member,フィールド削除（移行）,instance フィールドが削除され、instance_name に統合されました。,同上（instance_name への移行が必要です）。
リソース,google_bigtable_table_iam_policy,フィールド削除（移行）,instance フィールドが削除され、instance_name に統合されました。,同上（instance_name への移行が必要です）。
リソース,google_billing_budget,フィールド動作変更,budget_filter.credit_types および budget_filter.subaccounts が Optional+Computed から Optional のみに変更されました。,API デフォルト値をエクスポートしないフィールドだったため、実質的な挙動への影響はなく、設定の修正も不要です。
リソース,google_cloudfunctions2_function,フィールド制約変更 / 参照専用化,event_trigger.event_type が必須になり、service_config.service が参照専用に変更されました。,event_trigger 構成時に event_type の指定が必須となりました。また、service_config.service は参照専用（出力のみ）になったため、アップグレード後に設定から削除してください。
リソース,google_cloud_run_v2_worker_pool,フィールド削除,template.containers.depends_on フィールドが削除されました。,アップグレード後、設定ファイルから template.containers.depends_on を削除してください。
リソース,google_colab_runtime_template,フィールド削除,post_startup_script_config フィールドが削除されました。,アップグレード後、設定ファイルから post_startup_script_config を削除してください。
リソース,google_compute_instance_template,デフォルト値削除,disk.type、disk.mode、disk.interface がプロバイダのデフォルト値を使用しなくなりました。,これらのディスクパラメータはプロバイダ側のデフォルトに依存せず、API がデフォルト値を設定するようになります。詳細は API ドキュメントを参照してください。
リソース,google_compute_packet_mirroring,型変換（Set化）,subnetworks および instances フィールドが Set（セット）型に変換されました。,リストからセットに変更されました。ネストされたオブジェクトにアクセスする場合は、for_each を使用するか、設定内でローカルにリスト/配列に変換する必要があります。
リソース,google_compute_region_instance_template,デフォルト値削除,disk.type、disk.mode、disk.interface がプロバイダのデフォルト値を使用しなくなりました。,同上。
リソース,google_compute_router,型変換（Set化）,advertised_ip_ranges 各フィールドが Set（セット）型に変換されました。,ネストされたオブジェクト内の値にアクセスする際は、for_each を使用するか、設定内でローカルにリスト/配列に変換する必要があります。
リソース,google_compute_subnetwork,フィールド削除,enable_flow_logs フィールドが削除されました。,enable_flow_logs が削除され、log_config フィールドに一本化されました。
リソース,google_gke_hub_feature_membership,フィールド削除,configmanagement.binauthz フィールドが削除されました。,アップグレード後、設定ファイルから configmanagement.binauthz を削除してください。
リソース,google_gke_hub_membership,フィールド削除,description フィールドが削除されました。,アップグレード後、設定ファイルから description を削除してください。
リソース,google_memorystore_instance,フィールド削除,allow_fewer_zones_deployment フィールドが削除されました。,ユーザーが設定不可能なフィールドだったため削除されました。
リソース,google_network_services_lb_traffic_extension,フィールド制約変更,load_balancing_scheme フィールドが必須（required）になりました。,このリソースが機能するために元々必要な項目であったため、既存の設定への影響はありません。
リソース,google_notebooks_location,リソース削除,リソースが完全に削除されました。,動作していなかったリソースであるため、設定から安全に削除できます。
リソース,google_project_service,デフォルト値削除,disable_on_destroy のデフォルト値（true）が削除されました。,デフォルトで true になっていたことで、単一リソースの削除時にプロジェクト全体のAPIが無効化されるというリスクを回避するための変更です。今後はリソースを削除しても状態（State）から除外されるだけで、API自体は有効なまま残ります。以前と同じ挙動（リソース削除時にAPIも無効化する）を望む場合は、明示的に disable_on_destroy = true と指定してください。
リソース,google_redis_cluster,フィールド削除,allow_fewer_zones_deployment フィールドが削除されました。,ユーザー設定不可能であったため削除されました。
リソース,google_sql_user,フィールド制約,password_wo と password_wo_version は同時に指定する必要があります。,書込専用（write-only）フィールドの挙動標準化のための変更です。更新忘れを防ぐため、必ず両方のフィールドをセットで記述する必要があります。
リソース,google_secure_source_manager_instance,動作変更（削除保護）,deletion_policy のデフォルト値が PREVENT に変更されました。,意図しない削除を防ぐため、デフォルト値が PREVENT（防止）に変更されました。アップグレード後のリフレッシュ時に、既存のリソースも設定で明示していない限り PREVENT が適用されます。
リソース,google_secure_source_manager_repository,動作変更（削除保護）,deletion_policy のデフォルト値が PREVENT に変更されました。,同上。
リソース,google_storage_transfer_job,バリデーション強化,一部パスフィールドの先頭にスラッシュ（/）を使用することが禁止されました。,transfer_spec.gcs_data_sink.path、transfer_spec.gcs_data_source.path、replication_spec.gcs_data_source.path、および replication_spec.gcs_data_sink.path は先頭に / 文字を含めることができなくなりました。
リソース,google_storage_bucket,型変換,retention_period フィールドのデータ型が string（文字列）に変更されました。,"より大きな保持期間値を処理できるように型が変更されました。Terraformの型自動変換機能によりほとんどの構成でそのままでも動作しますが、明示的にダブルクォーテーションで囲んで設定（例: retention_period = ""10""）することが推奨されます。"
リソース,google_storage_notification,プラグインフレームワーク移行 & 形式厳格化,Plugin Framework への移行、および topic フィールドのフォーマット制限が適用されました。,SDKv2 から Plugin Framework に移行されました。topic に指定するフォーマットは projects/{{project}}/topics/{{topic}} 形式のみ許可され、従来の完全修飾 API フォーマット（//pubsub.googleapis.com/...）はバリデーションエラーになります。アップグレード時に State の自動移行は行われますが、設定ファイルの記述を手動で更新する必要があります。
リソース,google_tpu_node,リソース削除,google_tpu_node リソースが削除されました。,TPU VM アーキテクチャへの移行に伴い削除されました。今後は google_tpu_v2_vm を使用してください。移行の詳細は Google Cloud の公式ガイドを参照してください。
リソース,google_vertex_ai_endpoint,フィールド削除,GA（正式リリース）プロバイダから enable_secure_private_service_connect が削除されました。,GA版 API で本機能が提供されていないため削除されました（ベータ版プロバイダでは引き続き利用可能）。
リソース,google_vertex_ai_index,フィールド制約変更,metadata および metadata.config が必須（required）に変更されました。,リソース動作に不可欠なフィールドのため明確に必須化されました。既存の正常な設定に変更は不要です。
