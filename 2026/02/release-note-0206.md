
# Title: February 04, 2026 
Link: https://docs.cloud.google.com/release-notes#February_04_2026<br>
# BigQuery
## Change
原文: Data transfers from the YouTube Channel and YouTube Content Owner data sources now support reach reports. For more information, see YouTube Channel report transformation and YouTube Content Owner report transformation.
説明: BigQuery Data Transfer Service において、YouTube Channel および YouTube Content Owner のデータソースからのデータ転送が、新たにリーチレポート (reach reports) に対応しました。これにより、YouTube 関連のデータをBigQueryに転送する際に、より詳細な指標を扱えるようになります。
影響有無: **影響なし（ポジティブな影響）**
本変更は、既存機能に新たなレポートタイプが追加されたものであり、既存のデータ転送設定やワークロードに直接的な影響はありません。YouTube関連のデータをBigQueryに転送しており、今後リーチレポートによる分析を行いたいユーザーにとっては、利用可能な機能が拡張されるためポジティブな影響となります。
対処方法: 現在YouTube ChannelまたはYouTube Content Ownerのデータ転送を利用している場合でも、特段の対応は不要です。新しくリーチレポートを活用したい場合は、公式ドキュメントを参照し、必要に応じて転送設定やクエリを調整してください。
用語説明:
*   **データ転送 (BigQuery Data Transfer Service):** Google Cloudのサービスで、Google SaaSサービス（Google Ads, Google Analytics, YouTubeなど）やサードパーティのデータソースからBigQueryへ定期的にデータを自動でロードする機能です。
*   **YouTube Channel data source:** 特定のYouTubeチャンネルのパフォーマンスデータ（視聴回数、視聴時間、視聴者層など）をBigQueryに転送するためのデータソースです。
*   **YouTube Content Owner data source:** YouTubeのコンテンツ所有者（Content Owner）レベルでのデータ（収益、著作権クレーム、アセットパフォーマンスなど）をBigQueryに転送するためのデータソースです。
*   **リーチレポート (Reach reports):** YouTubeコンテンツがユニークユーザーにどの程度到達したかを示す指標を提供するレポートです。通常、広告キャンペーンの到達度やブランド認知度を測定するために利用されます。

---

# Google Kubernetes Engine
## Change
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
説明: GKEクラスターの利用可能なバージョンが更新されました。これにより、新規クラスターの作成時や、既存クラスターのコントロールプレーンおよびノードの手動アップグレード時に、新しいバージョンを選択できるようになりました。
影響有無: **影響なし（ポジティブな影響）**
このアナウンスは、GKEの新しいバージョンが利用可能になったことを通知するものです。既存のクラスターの動作に直接的な影響はありません。最新バージョンへのアップグレードが可能になることで、新機能の利用、パフォーマンスの改善、セキュリティの強化などの恩恵が受けられます。
対処方法: GKEクラスターの運用ポリシーに基づき、計画的なアップグレードを検討してください。アップグレードを行う前に、新しいKubernetesバージョンのリリースノートを確認し、アプリケーションや構成ファイルとの互換性を検証することを推奨します。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image: (table follows)
説明: 今回のリリースには、Container-Optimized OS (COS) イメージが更新されたGKEバージョンが含まれています。これらの更新されたイメージは累積的なものであり、前回のGKEリリース以降にリリースされた全てのCOSバージョンからのセキュリティ修正が組み込まれています。提供されているGKEバージョンと、それに対応するCOSイメージのセキュリティリリースノートへのリンクが示されています。
影響有無: **影響なし（ポジティブな影響）**
ノードイメージのセキュリティ修正が含まれるため、クラスター全体のセキュリティ体制が向上します。これは既存のワークロードにネガティブな影響を与えるものではなく、積極的にアップグレードを検討すべきポジティブな変更です。
対処方法: GKEクラスターのコントロールプレーンおよびノードプールを、これらの更新されたCOSイメージを使用する新しいGKEバージョンへアップグレードすることを強く推奨します。これにより、最新のセキュリティ修正が適用され、潜在的な脆弱性が解消されます。GKEの自動アップグレードが有効な場合は、メンテナンスウィンドウの設定を確認してください。

## Change (Extended channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - Version 1.34.3-gke.1051003 is now the default version for cluster creation in the Extended channel. - The following versions are now available in the Extended channel: ... - The following versions are no longer available in the Extended channel: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
説明: Extendedチャネルにおいて、GKEバージョンの更新が行われました。新規クラスター作成時のデフォルトバージョンが `1.34.3-gke.1051003` に変更され、Extendedチャネルで利用可能なバージョンリストが更新されました。同時に、一部の旧バージョンは利用不可になりました。また、このチャネルを利用しているクラスターの自動アップグレードターゲットが更新されました。
影響有無: **一部影響あり（自動アップグレードの挙動変更、サポート終了バージョンの確認）**
*   **自動アップグレードの挙動変更:** Extendedチャネルで自動アップグレードが有効になっている場合、メンテナンスウィンドウ内であれば、クラスターのコントロールプレーンおよびノードが新しいターゲットバージョンに自動的にアップグレードされる可能性があります。これにより、アプリケーションの互換性確認が必要になる場合があります。
*   **サポート終了バージョンの確認:** 既存クラスターが「利用不可になったバージョン」で稼働している場合、計画的なアップグレードが必要です。サポート終了バージョンを使い続けると、セキュリティリスクやサポート対象外となる可能性があります。
*   **新規クラスター作成:** 新規クラスターは新しいデフォルトバージョンで作成されます。
対処方法:
1.  **GKEクラスターバージョンの確認:** 現在稼働中のGKEクラスターがExtendedチャネルに属しているか、またそのバージョンが提供終了リストに含まれていないか確認してください。
2.  **自動アップグレード設定の確認:** 自動アップグレードが有効になっている場合、メンテナンスウィンドウや除外設定を確認し、予期せぬタイミングでのアップグレードや業務影響を避けるための計画を立ててください。
3.  **互換性検証:** 自動アップグレードまたは手動アップグレードの前に、ターゲットとなる新しいGKEバージョン（特にKubernetesマイナーバージョン）におけるAPIの変更や非推奨化された機能を確認し、アプリケーションが互換性を持つことをテスト環境で十分に検証してください。

## Change (Rapid channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - Version 1.35.0-gke.2232000 is now the default version for cluster creation in the Rapid channel. - The following versions are now available in the Rapid channel: ... - The following versions are no longer available in the Rapid channel: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
説明: Rapidチャネルにおいて、GKEバージョンの更新が行われました。新規クラスター作成時のデフォルトバージョンが `1.35.0-gke.2232000` に変更され、Rapidチャネルで利用可能なバージョンリストが更新されました。同時に、一部の旧バージョンは利用不可になりました。また、このチャネルを利用しているクラスターの自動アップグレードターゲットが更新されました。
影響有無: **一部影響あり（自動アップグレードの挙動変更、サポート終了バージョンの確認）**
*   **自動アップグレードの挙動変更:** Rapidチャネルで自動アップグレードが有効になっている場合、メンテナンスウィンドウ内であれば、クラスターのコントロールプレーンおよびノードが新しいターゲットバージョンに自動的にアップグレードされる可能性があります。このチャネルは更新頻度が高いため、より頻繁な互換性確認が必要となる可能性があります。
*   **サポート終了バージョンの確認:** 既存クラスターが「利用不可になったバージョン」で稼働している場合、計画的なアップグレードが必要です。
*   **新規クラスター作成:** 新規クラスターは新しいデフォルトバージョンで作成されます。
対処方法: Extendedチャネルと同様に、以下の対応を推奨します。
1.  **GKEクラスターバージョンの確認:** 現在稼働中のGKEクラスターがRapidチャネルに属しているか、またそのバージョンが提供終了リストに含まれていないか確認してください。
2.  **自動アップグレード設定の確認:** 自動アップグレードが有効になっている場合、メンテナンスウィンドウや除外設定を確認し、予期せぬタイミングでのアップグレードや業務影響を避けるための計画を立ててください。
3.  **互換性検証:** 自動アップグレードまたは手動アップグレードの前に、ターゲットとなる新しいGKEバージョンにおけるAPIの変更や非推奨化された機能を確認し、アプリケーションが互換性を持つことをテスト環境で十分に検証してください。RapidチャネルはKubernetesの最新版に追従するため、より厳密な互換性検証が求められる場合があります。

## Change (Regular channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - Version 1.34.3-gke.1051003 is now the default version for cluster creation in the Regular channel. - Version 1.33.5-gke.2228001 is now available in the Regular channel. - The following versions are no longer available in the Regular channel: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
説明: Regularチャネルにおいて、GKEバージョンの更新が行われました。新規クラスター作成時のデフォルトバージョンが `1.34.3-gke.1051003` に変更され、一部の新しいバージョンが利用可能になりました。同時に、一部の旧バージョンは利用不可になりました。また、このチャネルを利用しているクラスターの自動アップグレードターゲットが更新されました。
影響有無: **一部影響あり（自動アップグレードの挙動変更、サポート終了バージョンの確認）**
*   **自動アップグレードの挙動変更:** Regularチャネルで自動アップグレードが有効になっている場合、メンテナンスウィンドウ内であれば、クラスターのコントロールプレーンおよびノードが新しいターゲットバージョンに自動的にアップグレードされる可能性があります。
*   **サポート終了バージョンの確認:** 既存クラスターが「利用不可になったバージョン」で稼働している場合、計画的なアップグレードが必要です。
*   **新規クラスター作成:** 新規クラスターは新しいデフォルトバージョンで作成されます。
対処方法: Extendedチャネルと同様に、以下の対応を推奨します。
1.  **GKEクラスターバージョンの確認:** 現在稼働中のGKEクラスターがRegularチャネルに属しているか、またそのバージョンが提供終了リストに含まれていないか確認してください。
2.  **自動アップグレード設定の確認:** 自動アップグレードが有効になっている場合、メンテナンスウィンドウや除外設定を確認し、予期せぬタイミングでのアップグレードや業務影響を避けるための計画を立ててください。
3.  **互換性検証:** 自動アップグレードまたは手動アップグレードの前に、ターゲットとなる新しいGKEバージョンにおけるAPIの変更や非推奨化された機能を確認し、アプリケーションが互換性を持つことをテスト環境で十分に検証してください。

## Change (Stable channel)
原文: Note: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones. - Version 1.33.5-gke.2100001 is now the default version for cluster creation in the Stable channel. - The following versions are now available in the Stable channel: ... - The following versions are no longer available in the Stable channel: ... - Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: ...
説明: Stableチャネルにおいて、GKEバージョンの更新が行われました。新規クラスター作成時のデフォルトバージョンが `1.33.5-gke.2100001` に変更され、一部の新しいバージョンが利用可能になりました。同時に、一部の旧バージョンは利用不可になりました。また、このチャネルを利用しているクラスターの自動アップグレードターゲットが更新されました。
影響有無: **一部影響あり（自動アップグレードの挙動変更、サポート終了バージョンの確認）**
*   **自動アップグレードの挙動変更:** Stableチャネルで自動アップグレードが有効になっている場合、メンテナンスウィンドウ内であれば、クラスターのコントロールプレーンおよびノードが新しいターゲットバージョンに自動的にアップグレードされる可能性があります。このチャネルは最も安定したバージョンが提供されるため、変更頻度は他のチャネルより低いですが、アプリケーションの互換性確認は依然として重要です。
*   **サポート終了バージョンの確認:** 既存クラスターが「利用不可になったバージョン」で稼働している場合、計画的なアップグレードが必要です。
*   **新規クラスター作成:** 新規クラスターは新しいデフォルトバージョンで作成されます。
対処方法: Extendedチャネルと同様に、以下の対応を推奨します。
1.  **GKEクラスターバージョンの確認:** 現在稼働中のGKEクラスターがStableチャネルに属しているか、またそのバージョンが提供終了リストに含まれていないか確認してください。
2.  **自動アップグレード設定の確認:** 自動アップグレードが有効になっている場合、メンテナンスウィンドウや除外設定を確認し、予期せぬタイミングでのアップグレードや業務影響を避けるための計画を立ててください。
3.  **互換性検証:** 自動アップグレードまたは手動アップグレードの前に、ターゲットとなる新しいGKEバージョンにおけるAPIの変更や非推奨化された機能を確認し、アプリケーションが互換性を持つことをテスト環境で十分に検証してください。

---
用語説明 (GKE共通):
*   **GKE (Google Kubernetes Engine):** Google Cloudが提供するマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **コントロールプレーン (Control Plane):** Kubernetesクラスターの制御を司るコンポーネント群（APIサーバー、スケジューラー、コントローラーマネージャーなど）です。
*   **ノード (Node):** アプリケーションのコンテナ（Pod）が実際に稼働する仮想マシンまたは物理マシンです。
*   **Container-Optimized OS (COS):** GoogleがGKEノード向けに最適化して提供するLinuxベースのオペレーティングシステムイメージです。セキュリティと効率性を重視しています。
*   **リリースチャネル (Release Channel):** GKEクラスターのバージョンアップグレードの頻度と安定性を選ぶための設定です。「Rapid」「Regular」「Stable」「Extended」などのチャネルがあり、それぞれ提供されるバージョンの新しさや安定性が異なります。
    *   **Rapid (ラピッド) チャネル:** 最も早く新機能や最新のKubernetesバージョンが提供されるチャネル。開発環境や最新機能を試したい場合に適します。
    *   **Regular (レギュラー) チャネル:** ラピッドチャネルより安定性が高く、幅広いユーザーに推奨される一般的なチャネル。
    *   **Stable (ステーブル) チャネル:** 最も安定したバージョンが提供されるチャネル。本番環境での利用に最も推奨されます。
    *   **Extended (エクステンデッド) チャネル:** 特定のマイナーバージョンを長期的に利用したい場合に選択されるチャネル。サポート期間が他のチャネルよりも長いです。
*   **自動アップグレード (Auto-upgrade):** GKEクラスターのコントロールプレーンとノードが、Googleによって自動的に新しいバージョンにアップグレードされる機能です。
*   **メンテナンスウィンドウ (Maintenance Window):** 自動アップグレードやその他のメンテナンス作業が許可される時間帯を指定する設定です。
*   **メンテナンス除外 (Maintenance Exclusions):** 特定の期間、自動アップグレードなどのメンテナンス作業を一時的に停止する設定です。
*   **非推奨API (Deprecated APIs):** Kubernetesのバージョンアップに伴い、将来的に削除されることが決定しているAPIです。これらのAPIを使用しているアプリケーションは、新しいAPIへの移行が必要です。
# Title: February 03, 2026 
Link: https://docs.cloud.google.com/release-notes#February_03_2026<br>
# BigQuery
## Announcement
原文: Gemini in BigQuery now processes data in the same jurisdiction (`US` or `EU`) as your BigQuery datasets, or based upon user-specified location settings. For more information, see Where Gemini BigQuery processes your data.
[Where Gemini BigQuery processes your data](https://docs.cloud.google.com/bigquery/docs/gemini-locations)

説明:
このアナウンスは、BigQueryに統合されたAI機能である「Gemini in BigQuery」におけるデータ処理のロケーション（管轄地域）に関するものです。Gemini in BigQueryがデータを処理する際、BigQueryデータセットが存在するのと同じ管轄地域（米国またはEU）内で処理されるか、ユーザーが明示的に指定したロケーション設定に基づいて処理されるようになりました。これにより、データの所在地に関する要件（データレジデンシー）をより明確に管理できるようになります。

影響有無:
**影響はありません。**
このアナウンスは、BigQueryデータセットのロケーションとGeminiの処理ロケーションの連携を強化し、ユーザーがデータ処理のロケーションをより明確にコントロールできるようになったことを示すものです。既存のBigQueryの利用方法やデータ処理のワークフローに直接的な変更を強制するものではなく、後方互換性が維持されています。特に、データレジデンシー要件が厳しい環境においては、データの処理ロケーションが明確になることで、コンプライアンス上の懸念が解消される可能性があります。

対処方法:
既存のワークロードに対する直接的な対応は不要です。
ただし、データレジデンシー要件が厳格な環境でGemini in BigQueryの利用を検討している場合、または将来的に利用する可能性がある場合は、提供されているリンク先のドキュメント「[Where Gemini BigQuery processes your data](https://docs.cloud.google.com/bigquery/docs/gemini-locations)」を参照し、ご自身のデータ処理ロケーション要件が満たされているかを確認することを推奨します。

用語説明:
*   **Gemini in BigQuery**: Google Cloudの生成AIモデル「Gemini」がBigQueryに統合された機能群を指します。これにより、SQLクエリの生成支援、データ分析に関する質問への回答、データの要約など、AIを活用したデータ分析が可能になります。
*   **Jurisdiction (管轄/地域)**: データが処理または保存される地理的な場所を指します。国の法律や規制、企業のコンプライアンス要件（特にデータレジデンシー）において重要な概念です。
*   **Data Residency (データレジデンシー)**: 特定のデータが物理的に特定の地理的領域内に存在し、かつその領域内で処理されることを保証する要件を指します。国や地域の法律、業界規制、企業の内部ポリシーなどによって義務付けられる場合があります。
*   **User-specified location settings**: Google Cloudサービスにおいて、ユーザーが明示的にリソースの作成場所やデータ処理のロケーションを指定できる設定を指します。これにより、ユーザーは自身のコンプライアンスやパフォーマンス要件に基づいて、データの物理的な配置をコントロールできます。
# Title: February 02, 2026 
Link: https://docs.cloud.google.com/release-notes#February_02_2026<br>
Google Cloudのインフラエンジニアとして、リリースノートに基づき、構築済みのサービスへの影響有無を調査しました。

---

# API Gateway
## Change
原文: API Gateway can now be connected to Apigee API hub instances that use VPC Service Controls.
[connected to Apigee API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-connect)
[VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc)

説明：
この変更により、API Gatewayが、VPC Service Controlsで保護されたApigee API hubインスタンスと接続できるようになりました。これにより、VPC Service Controlsを適用している環境においても、API Gatewayを介してApigee API hubで管理されているAPIを利用することが可能になります。

影響有無：
**影響なし**
この変更は新機能の追加であり、既存のAPI GatewayおよびApigee API hubの構成や動作に直接的な変更や非互換性をもたらすものではありません。現在VPC Service Controlsを利用していない環境や、API GatewayとApigee API hubの連携を行っていない環境には影響はありません。

対処方法：
特段の対処は不要です。VPC Service Controlsを利用してセキュリティ境界を確立している環境で、API Gateway経由でApigee API hubに接続したい場合に、この新機能を活用することを検討してください。詳細な設定方法については、提供されたドキュメントリンク（[connected to Apigee API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-connect)）を参照してください。

用語説明：
*   **API Gateway:** Google Cloud上でAPIを安全かつスケーラブルに公開・管理するためのフルマネージドサービスです。バックエンドサービスへのルーティング、認証、レート制限などを提供します。
*   **Apigee API hub:** APIのデザイン、管理、公開、監視を支援するAPI管理プラットフォームです。APIエコシステムの構築と運用を簡素化します。
*   **VPC Service Controls:** Google Cloudのデータ漏洩（Data Exfiltration）リスクを軽減するためのセキュリティ機能です。サービス境界を設定することで、サポート対象のGoogle Cloudサービスが、許可された境界の外にあるネットワークからのアクセスや、データ移動を防ぎます。

---

# Apigee X
## Issue
原文: **Known Issue:** 480997525 - Proxy calls fail with `The URI contain illegal characters` error after Netty upgrade
[480997525 - Proxy calls fail with `The URI contain illegal characters` error after Netty upgrade](https://docs.cloud.google.com/apigee/docs/release/known-issues#480997525)

説明：
Apigee Xにおいて、Netty（ネットワーク通信フレームワーク）のアップグレード後に、プロキシ呼び出しが「The URI contain illegal characters」（URIに不正な文字が含まれています）というエラーで失敗するという既知の問題が報告されています。これは、特定のURIパターンを持つリクエストが正しく処理されない可能性があることを示しています。

影響有無：
**潜在的な影響あり**
Apigee Xをご利用中の環境で、もし最近Nettyのアップグレードが行われ、かつ、プロキシ呼び出しが`The URI contain illegal characters`というエラーで失敗している場合は、この既知の問題の影響を受けている可能性があります。現在、このエラーが発生していない場合でも、将来的に特定のURIパターンを持つリクエストが同様のエラーを引き起こす可能性があります。

対処方法：
この問題は「Known Issue」（既知の問題）として報告されており、Google Cloudが認識し対応を進めている可能性があります。現時点では、リリースノートに具体的な回避策や修正バージョンに関する情報が記載されていません。
もし現在この問題に直面している場合は、以下の対応を検討してください。
1.  **詳細情報の確認:** 提供されたリンク（[480997525 - Proxy calls fail with `The URI contain illegal characters` error after Netty upgrade](https://docs.cloud.google.com/apigee/docs/release/known-issues#480997525)）を参照し、追加の情報や回避策が公開されていないか確認してください。
2.  **Google Cloudサポートへの問い合わせ:** サービスに重大な影響が出ている場合は、Google Cloudサポートに具体的な状況と発生しているエラーメッセージを添えて問い合わせてください。
3.  **定期的な監視:** 今後のリリースノートやApigee Xのドキュメントを定期的に確認し、この問題の修正や回避策に関する情報が公開されていないか注意してください。

用語説明：
*   **Apigee X:** Google Cloud上に構築された、API管理の最新世代プラットフォームです。Google Cloudの機能との統合が強化され、スケーラビリティと信頼性を提供します。
*   **Proxy calls:** API管理において、クライアントからのAPIリクエストをApigeeが受け取り、バックエンドのターゲットサービスへ転送（プロキシ）する処理のことです。
*   **Netty:** Javaで開発された高性能なネットワークアプリケーションフレームワークです。非同期イベント駆動型モデルを採用し、高スループットと低レイテンシのネットワーク通信を可能にします。多くのWebサービスや分散システムで基盤技術として利用されています。
*   **URI (Uniform Resource Identifier):** インターネット上のリソースを一意に識別するための文字列です。URIはURL（Uniform Resource Locator）やURN（Uniform Resource Name）の総称です。`The URI contain illegal characters`は、指定されたURIの構文がRFC（Request for Comments）などの仕様に準拠していない場合に発生するエラーです。