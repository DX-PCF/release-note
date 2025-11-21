
# Title: November 19, 2025 
Link: https://docs.cloud.google.com/release-notes#November_19_2025<br>
# AlloyDB for PostgreSQL

## Changed

原文: The upper limit of the query plans captured per minute is enhanced to 200. For more information, see Improve query performance using advanced query insights features for AlloyDB.

説明：
AlloyDB for PostgreSQL の「Advanced Query Insights」機能において、1分間にキャプチャ（取得）できるクエリプランのデータ数の上限が、これまでの値から200に引き上げられました。これにより、より多くのクエリ実行計画を詳細に分析できるようになり、クエリパフォーマンスの改善に役立つ洞察を深めることが可能になります。

影響有無：
**影響なし（ポジティブな影響）**

この変更は機能の強化であり、既存のサービスに対して負の影響を与えるものではありません。むしろ、AlloyDB のクエリ分析能力が向上するため、Query Insights 機能を利用している場合にはより詳細なデータに基づいた分析が可能になり、パフォーマンスチューニングに役立ちます。利用していない場合でも、将来的に活用する際にメリットを享受できます。

対処方法：
**ユーザー側での直接的な対処は不要です。**

この変更は自動的に適用されるため、特別な操作は必要ありません。
Query Insights を積極的に活用している場合は、この改善により収集されるデータ量が増えることで、より精密なクエリ最適化の機会が得られます。必要に応じて、AlloyDB の Query Insights 機能に関するドキュメントを参照し、新しい上限を活かした分析手法を検討することができます。

用語説明：
*   **Query Plans (クエリプラン):** データベースがSQLクエリを実行する際に、どのインデックスを使用するか、どのテーブルをどのような順序で結合するかといった、最適な実行手順を定義した計画のことです。データベースのオプティマイザによって生成されます。
*   **Query Insights (クエリインサイト):** データベースのクエリパフォーマンスを監視・分析し、ボトルネックを特定するための機能です。AlloyDBでは「Advanced Query Insights」として提供され、クエリの実行統計、待機イベント、クエリプランなどを可視化します。
*   **Upper limit (上限):** ここでは、Query Insights 機能で1分あたりに取得できるクエリプランの最大数を指します。この上限が引き上げられることで、より多くのクエリプランをサンプリングし、分析精度を高めることができます。
# Title: November 18, 2025 
Link: https://docs.cloud.google.com/release-notes#November_18_2025<br>
# Cloud Service Mesh

## Announcement

**原文:**
The following rollouts have completed for managed Cloud Service Mesh:
- 1.21.6-asm.4 has rolled out to the rapid release channel.
- 1.20.8-asm.56 has rolled out to the regular release channel.
- 1.19.10-asm.52 has rolled out to the stable release channel.
- CNI and MDPC version 1.20.8-asm.56 has rolled out to all release channels.

While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

**説明:**
Google Cloudが提供するマネージドCloud Service Meshにおいて、以下のバージョンアップロールアウトが完了しました。

*   **リリースチャネルごとのAnthos Service Mesh (ASM) バージョンアップ:**
    *   Rapidリリースチャネルには `1.21.6-asm.4` がデプロイされました。
    *   Regularリリースチャネルには `1.20.8-asm.56` がデプロイされました。
    *   Stableリリースチャネルには `1.19.10-asm.52` がデプロイされました。
*   **CNI (Container Network Interface) および MDPC (Managed Data Plane Controller) のバージョンアップ:**
    *   すべてのリリースチャネルで `1.20.8-asm.56` がデプロイされました。

マネージドデータプレーンは、ワークロードの再起動によってEnvoy Proxyを自動的に更新しますが、`StatefulSet` および `Job` としてデプロイされているワークロードについては、手動での再起動が必要です。

**影響有無:**
本リリースノートは、Cloud Service Meshのバージョンアップロールアウト完了に関するアナウンスであり、既存の機能動作への直接的な変更や非互換性の導入を示すものではありません。

*   **Cloud Service Meshを現在利用している場合:**
    *   マネージドデータプレーンの自動更新により、多くのEnvoy Proxyは自動的に最新バージョンに更新されます。
    *   ただし、お使いの環境でCloud Service Meshが有効化されており、かつ`StatefulSet`または`Job`としてデプロイされたワークロードがサービスメッシュによって管理されている（サイドカーが注入されている）場合、それらのワークロードのEnvoy Proxyを更新するためには手動での再起動が必要です。
*   **Cloud Service Meshを現在利用していない場合:**
    *   影響はありません。
*   **Google Cloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) への影響:**
    *   Composer環境自体が直接Cloud Service Meshを利用することは一般的ではありません。しかし、ComposerのDAGから呼び出すカスタムアプリケーションがGKE上にデプロイされており、そのアプリケーションにCloud Service Meshが適用されている場合は、上記の「Cloud Service Meshを現在利用している場合」の条件に準じて影響がある可能性があります。

**対処方法:**
1.  **Cloud Service Meshの利用状況確認:** ご利用のGoogle Cloudプロジェクトにおいて、Cloud Service Mesh（Anthos Service Mesh）が有効化され、GKEクラスタにデプロイされているか確認してください。
2.  **`StatefulSet`および`Job`の有無確認:** Cloud Service Meshが有効なGKEクラスタにおいて、`StatefulSet`または`Job`としてデプロイされているワークロードが存在し、それらがService Meshによって管理されている（例：サイドカープロキシが注入されている）か確認してください。
3.  **手動再起動の実施:**
    *   もし該当する`StatefulSet`または`Job`が存在し、かつEnvoy Proxyの更新が必要な場合は、これらのワークロードを手動で再起動してください。
    *   `Deployment`などの他のワークロードタイプについては、マネージドデータプレーンが自動的に更新を処理するため、特別な操作は不要です。
4.  **影響がない場合の確認:** 上記の条件に該当するワークロードがない場合、特別な対処は不要です。

**用語説明:**
*   **Cloud Service Mesh (Anthos Service Mesh - ASM):** Google Cloudが提供する、Google Kubernetes Engine (GKE) 上で動作するサービスメッシュのマネージドサービスです。Istioをベースにしており、サービス間のトラフィック管理、セキュリティ、観測性を向上させます。
*   **Release Channel:** Google Kubernetes Engine (GKE) やAnthos Service MeshなどのGoogle Cloudサービスにおける、ソフトウェア更新の提供ペースと安定性を示すチャネルです。
    *   **Rapid:** 最新の機能が最も早く利用できますが、安定性は他のチャネルより劣る可能性があります。
    *   **Regular:** バランスの取れた更新サイクルで、新機能と安定性の両方を考慮します。
    *   **Stable:** 最も安定性が重視され、検証された更新が提供されます。
*   **CNI (Container Network Interface):** Kubernetes環境において、コンテナのネットワーク接続を設定するための標準的なインターフェースです。Pod間の通信や外部ネットワークとの接続を可能にします。
*   **MDPC (Managed Data Plane Controller):** マネージドAnthos Service Meshのデータプレーン（Envoy Proxyなど）のライフサイクル管理と設定配布を担うコントローラです。
*   **Envoy Proxy:** IstioやCloud Service Meshのデータプレーンとして使用される、高性能なオープンソースのサービスプロキシです。サービス間のトラフィックをインターセプトし、ルーティング、負荷分散、認証、ポリシー適用などの機能を提供します。
*   **StatefulSet:** Kubernetesのワークロードリソースの一種で、永続的な識別子、安定したホスト名、順序付けられたデプロイ/スケーリング/削除などを必要とするステートフルなアプリケーション（データベースなど）を管理するために使用されます。
*   **Job:** Kubernetesのワークロードリソースの一種で、完了するまで一度だけ実行されるタスク（バッチ処理など）を作成するために使用されます。タスクが成功すると、Podは終了します。
*   **Workload:** Kubernetesクラスタで実行されるアプリケーションやサービスの実体を表す広範な用語で、`Deployment`、`StatefulSet`、`Job`などが含まれます。
# Title: November 17, 2025 
Link: https://docs.cloud.google.com/release-notes#November_17_2025<br>
Google Cloudのリリースノートに基づき、各製品の変更点とお客様のサービスへの影響を調査しました。

---

# Apigee X

## Announcement

原文: On November 17, 2025, we released an updated version of Apigee (1-16-0-apigee-5).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigeeの新しいバージョン `1-16-0-apigee-5` が2025年11月17日にリリースされました。このリリースはすでに展開が開始されており、Google Cloudの全ゾーンへの完了には4営業日以上かかる可能性があります。展開が完了するまでは、一部のインスタンスで新しい機能や修正が利用できない場合があります。
影響有無: 影響あり。お客様のApigeeインスタンスは自動的にこの新しいバージョンに更新される可能性があります。更新が完了するまでは、特定の機能や修正が利用できない期間が発生する可能性があります。ただし、既存のAPIプロキシやAPIプロダクトの動作に直接的な変更を強制するものではありません。
対処方法: 特段の緊急対処は不要です。Apigeeインスタンスが自動的に更新されることを認識しておいてください。ロールアウト期間中は、新規開発や機能テストを行う際に、特定の機能がまだ利用できない可能性がある点に注意してください。

用語説明:
*   **Apigee X**: Google Cloud上で提供されるAPI管理プラットフォーム。APIのライフサイクル全体を管理し、セキュリティ、トラフィック管理、分析などを行います。
*   **Rollout**: ソフトウェアやシステムの新しいバージョンを段階的に展開していくプロセス。

## Fixed

原文: N/A - Updates to security, infrastructure, and libraries.

説明: セキュリティ、インフラストラクチャ、およびライブラリに対する一般的な更新が行われました。
影響有無: 影響なし。これはシステムの安定性やセキュリティを向上させるための一般的なメンテナンスであり、既存の動作に直接的な影響を与えるものではありません。
対処方法: 特段の対処は不要です。

## Security

原文: 454672970 - Added strict input validation to the `SetIntegrationRequest` policy.

説明: `SetIntegrationRequest` ポリシーに厳格な入力バリデーション（検証）が追加されました。これにより、ポリシーへの不正な入力を防ぎ、セキュリティが強化されます。
影響有無: 影響あり。`SetIntegrationRequest` ポリシーを利用しているAPIプロキシがある場合、これまで許容されていた不正な形式の入力が、この変更により拒否されるようになる可能性があります。
対処方法: `SetIntegrationRequest` ポリシーを使用しているAPIプロキシについて、ポリシーが処理する入力データが厳格なバリデーションルールに準拠しているか確認してください。もし準拠していないデータがある場合は、ポリシーが正しく動作しなくなるのを避けるため、事前に修正を施す必要があります。

用語説明:
*   **SetIntegrationRequest policy**: Apigeeのポリシーの一つで、バックエンドの統合（Integration）サービスに対してリクエストを構成・送信するために使用されます。
*   **Input Validation (入力バリデーション)**: プログラムやシステムへの入力データが、期待される形式、範囲、または内容に準拠しているかを確認するプロセス。セキュリティ強化の基本的な対策です。

---

# Cloud Composer

## Changed

原文: New Airflow builds are available in Cloud Composer 3:
[Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-3.1.0-build.2
[composer-3-airflow-3.1.0-build.2](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-0-build-2)

説明: Cloud Composer 3向けに新しいAirflowビルド `composer-3-airflow-3.1.0-build.2` が利用可能になりました。
影響有無: 影響なし。お客様の環境はCloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) を利用しているため、Cloud Composer 3に関するこの変更は直接的な影響を与えません。
対処方法: 特段の対処は不要です。将来的にCloud Composer 3へのアップグレードを検討する際に、この新しいAirflowバージョンを考慮に入れることになります。

用語説明:
*   **Cloud Composer**: Google Cloud上でApache Airflowをマネージドサービスとして提供するサービス。ワークフローのオーケストレーションに使用されます。
*   **Airflow build**: Cloud Composer環境を構築するための特定のAirflowバージョンと関連コンポーネントのパッケージ。

## Announcement

原文: All Cloud Composer environment's GKE clusters are set up with **maintenance exclusions** from December 16, 2025 to January 2, 2025. For more information, see Maintenance exclusions.
[Maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)

説明: 全てのCloud Composer環境の基盤となるGKE（Google Kubernetes Engine）クラスタに対して、**メンテナンス除外期間**が2025年12月16日から2025年1月2日まで設定されます。この期間中は、GKEクラスタに対する自動メンテナンス（アップグレードなど）が実施されません。
**注:** リリースノートの日付表記 "December 16, 2025 to January 2, 2025" は、通常の期間表記とは異なり、2025年の12月から2025年の1月という順序逆転が見られます。これは通常、年末年始（例えば2024年12月16日〜2025年1月2日、または2025年12月16日〜2026年1月2日）を指す場合の誤植である可能性が高いです。
影響有無: 影響あり。お客様のCloud Composer環境はGKEクラスタ上で動作しているため、このメンテナンス除外期間が適用されます。この期間中はGKEクラスタの自動メンテナンスが行われないため、計画的な運用の助けとなります。一方で、この期間中にセキュリティパッチや機能改善が適用されることはありません。
対処方法: この期間中はGKEクラスタの自動メンテナンスが停止するため、追加の対処は不要です。通常、この設定はサービスの安定稼働を目的としています。ただし、上記の日付の矛盾について、Google Cloudの公式アナウンスやドキュメントで再確認することをお勧めします。

用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービス。Cloud Composerは内部的にGKEクラスタを利用してAirflow環境を構築しています。
*   **Maintenance exclusions (メンテナンス除外期間)**: GKEクラスタの自動メンテナンス（バージョンアップグレード、パッチ適用など）が実施されない期間を設定する機能。これにより、サービスのダウンタイムや予期せぬ挙動を避けることができます。