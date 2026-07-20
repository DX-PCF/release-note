
# Title: July 16, 2026 
Link: https://docs.cloud.google.com/release-notes#July_16_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、構築済みのサービス（Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)）への影響調査結果を製品ごとにご報告いたします。

---

# Apigee X
## Announcement
原文: On July 16th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-10**, your instance will be updated to **1-17-0-apigee-10** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.
Note: Instances that meet either of the following two criteria will not be updated:
- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.
For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.

説明：
2026年7月16日より、メンテナンスウィンドウが設定されているApigeeインスタンスに対するメンテナンスアップデートが開始されます。
もしお客様のApigeeインスタンスがバージョン `1-17-0-apigee-10` 未満で、かつメンテナンスの優先ウィンドウが設定されている場合、今後7～21日以内に自動的に `1-17-0-apigee-10` へアップグレードされます。アップグレード予定日に関する通知は、今後2営業日以内に送信されます。
ただし、以下のいずれかの条件に該当するインスタンスはアップグレードされません。
*   既知の不具合 (Known Issue 445936920) に記載されているようなDNS設定ミスがある場合。
*   2025年10月16日のApigeeリリースノートで削除されたApigee Javaライブラリを使用している場合。

影響有無：**影響なし**
理由：今回のリリースノートはApigee Xに関するものであり、現在の環境でApigee Xの利用は確認されておりません。

対処方法：
Apigee Xをご利用の場合、メンテナンスウィンドウの設定を確認し、インスタンスのバージョンが `1-17-0-apigee-10` 未満であるかを確認してください。アップグレードされない条件（DNS設定ミス、削除されたJavaライブラリの使用）に該当しないかどうかも事前に確認することをお勧めします。

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームの最新バージョン。APIの設計、セキュア化、デプロイ、監視、分析を支援します。
*   **メンテナンスウィンドウ**: クラウドサービスプロバイダーがサービスに対してメンテナンス作業を行う期間を指定する機能です。これにより、ユーザーはサービスへの影響を最小限に抑えるための計画を立てることができます。
*   **インスタンス**: Apigee環境における特定のサービスまたはコンポーネントの実行単位です。
*   **DNS misconfiguration**: DNS（Domain Name System）設定に誤りがある状態を指します。これにより、ドメイン名からIPアドレスへの変換が正しく行われず、サービスへのアクセスに問題が生じる可能性があります。
*   **Apigee Java Library**: Apigeeのポリシーやカスタムコードで使用されるJavaライブラリ。一部のライブラリは非推奨または削除されることがあります。

---

# Compute Engine
## Change
原文: The following operations on the boot disk of a Compute Engine instance that has a service account attached no longer require the `iam.serviceAccounts.actAs` permission. In the following list, the boot disk of such an instance is referred to as the *source disk*.
- Creating a standard or archive snapshot of the source disk.
- Cloning the source disk.
- Creating a machine image of the instance.
- Creating a custom image of the source disk.
- Starting asynchronous replication of the source disk to another region.
- Creating a new disk when you create an instance, if the new disk is created from an instant snapshot of the source disk.

説明：
サービスアカウントがアタッチされたCompute Engineインスタンスのブートディスクに対し、以下の操作を行う際に `iam.serviceAccounts.actAs` 権限が不要になりました。これにより、IAMポリシーの権限をより絞り込むことが可能になります。
対象となる操作は以下の通りです。
*   ソースディスクの標準スナップショットまたはアーカイブスナップショットの作成。
*   ソースディスクのクローン作成。
*   インスタンスのマシンイメージの作成。
*   ソースディスクのカスタムイメージの作成。
*   ソースディスクから別のリージョンへの非同期レプリケーションの開始。
*   インスタンス作成時に新しいディスクを作成する場合で、その新しいディスクがソースディスクのインスタントスナップショットから作成される場合。

影響有無：**影響なし（ポジティブな影響の可能性あり）**
理由：Compute Engineインスタンスのブートディスク操作におけるIAM権限要件の緩和であり、既存のシステム動作に悪影響はありません。むしろ、セキュリティのベストプラクティスである最小権限の原則に則り、不要な権限を削除できる機会を提供します。Google Cloud Composerは内部でCompute Engineを使用しますが、ブートディスク操作のIAM権限を直接Composerユーザーが管理することは通常ありません。

対処方法：
今回の変更は権限の要件を緩和するものであり、既存の運用に影響を与えるものではありません。IAMポリシーを定期的に見直し、最小権限の原則を適用している場合は、この変更を受けて `iam.serviceAccounts.actAs` 権限が不要になるシナリオがないか確認し、IAMポリシーを最適化することを検討してください。

用語説明：
*   **Compute Engineインスタンス**: Google Cloud上で動作する仮想マシン（VM）です。
*   **サービスアカウント**: Google Cloudリソースにアクセスするための認証情報として使用される特別なアカウントです。人間ではなく、アプリケーションやVMインスタンスがGoogle Cloud APIを呼び出す際に使用します。
*   **`iam.serviceAccounts.actAs` 権限**: サービスアカウントの権限を借用して（「〜として振る舞う」）別の操作を実行することを許可するIAM権限です。この権限があることで、ユーザーやサービスが、本来のサービスアカウントが持つ権限を使って操作を行うことができます。
*   **ブートディスク**: オペレーティングシステムが格納され、インスタンスの起動に使用されるディスクです。
*   **スナップショット**: ディスクの特定時点での状態を保存したものです。バックアップや新しいディスクの作成に使用されます。
*   **クローン**: 既存のディスクの正確なコピーを作成する操作です。
*   **マシンイメージ**: Compute Engineインスタンスの完全なイメージ（ブートディスクとインスタンス設定を含む）を作成する機能です。
*   **カスタムイメージ**: ユーザーが独自のソフトウェアや設定を含むディスクイメージを作成する機能です。
*   **非同期レプリケーション**: ディスクのデータを非同期的に別のリージョンに複製するプロセスです。災害復旧などに利用されます。
*   **インスタントスナップショット**: 迅速にディスクのスナップショットを作成し、短時間で新しいディスクを作成できるようにする機能です。

---

# Google Kubernetes Engine
## Change (No channel, Stable, Regular, Rapid, Extended Channels の GKE バージョン更新)
原文: GKE cluster versions have been updated. (各チャンネルごとの詳細なバージョンリストと自動アップグレードターゲット)

説明：
Google Kubernetes Engine (GKE) の各リリースチャンネル（No channel, Stable, Regular, Rapid, Extended）において、新しいGKEバージョンが利用可能になり、同時に一部の古いバージョンが非推奨となりました。これにより、新しいクラスターの作成や既存クラスターのアップグレードに使用できるバージョンが更新されます。また、GKEの自動アップグレードターゲットも更新されています。

影響有無：**軽微な影響あり（情報提供）**
理由：
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) はGKEクラスター上で動作しますが、Composerが使用するGKEバージョンはGoogleによって管理されており、通常ユーザーが直接GKEのバージョンを選択またはアップグレードすることは少ないです。Composer 2.7.xは主にGKE 1.25.x、1.26.x、1.27.xなど比較的安定したバージョンで稼働しています（2024年4月時点）。
今回のGKEリリースノートでアナウンスされているバージョンは1.30.x〜1.36.xと、Composer 2.7.1が現在利用しているGKEバージョンよりも新しい範囲です。したがって、**現在のComposer環境が直ちにこれらの新しいバージョンに自動アップグレードされる可能性は低い**です。
ただし、GKEのバージョンサポートポリシーにより、非推奨となったバージョンは将来的にサポートが終了します。Composerが将来的にこれらの新しいGKEバージョンを採用する際、非推奨となったGKEバージョンからの移行が必要になる可能性があります。

対処方法：
現時点では、Google Cloud Composer 2の利用者として直接的な対処は不要です。ComposerはGKEバージョンを抽象化して提供しているため、GKEのバージョン管理はGoogle Cloud Composerサービス側で行われます。
今後、Google Cloud Composerのリリースノートで、ComposerがサポートするGKEバージョンの変更やアップグレードに関するアナウンスがないか、引き続き注意してください。これにより、将来的なComposerのアップグレードがスムーズに行われることを確認できます。

用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **リリースチャンネル (Release Channels)**: GKEクラスターのバージョンアップグレードの頻度と安定性を定義する仕組みです。Rapid、Regular、Stable、Extendedなどがあり、それぞれ新しいバージョンが利用可能になるまでの期間や安定性の保証レベルが異なります。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスターの管理部分で、クラスターの状態を維持し、ノードとポッドの動作を決定するコンポーネント群（例: APIサーバー、スケジューラー、コントローラーマネージャー）です。
*   **ノードプール (Node Pool)**: GKEクラスター内の同じ設定を持つVMインスタンス（ノード）のグループです。
*   **自動アップグレード (Auto Upgrade)**: GKEクラスターのコントロールプレーンやノードが自動的に新しいパッチまたはマイナーバージョンにアップグレードされる機能です。
*   **非推奨 (Deprecated)**: 今後新しいバージョンでの利用が推奨されず、将来的にサポートが終了する予定の機能やバージョンを指します。
*   **マイナーバージョン (Minor Version)**: Kubernetesのバージョン番号（例: v1.27.x）の真ん中の数字（27）が変更されるアップグレードです。機能追加やAPIの変更が含まれることがあります。
*   **パッチバージョン (Patch Version)**: Kubernetesのバージョン番号（例: v1.27.3）の最後の数字（3）が変更されるアップグレードです。主にバグ修正やセキュリティアップデートが含まれます。
*   **メンテナンス除外 (Maintenance Exclusions)**: GKEクラスターの自動アップグレードが行われない期間を一時的に設定する機能です。特定の時間帯や期間、アップグレードをブロックするために使用します。

---

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image.

説明：
今回のGKEリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたイメージには、前回のGKEリリース以降に公開された全てのCOSバージョンのセキュリティ修正が累積的に適用されています。

影響有無：**影響なし（ポジティブな影響）**
理由：GKE基盤のセキュリティが強化されるため、Composerを含むGKE上で稼働する全てのワークロードのセキュリティが向上します。既存の機能や運用に悪影響はありません。

対処方法：
特段の対処は不要です。GKEクラスターが新しいバージョンに更新される際に、これらのセキュリティ修正が適用されます。ComposerはGoogleがGKE基盤を管理しているため、自動的に最新のセキュリティパッチが適用されていきます。

用語説明：
*   **Container-Optimized OS (COS)**: コンテナの実行に最適化されたGoogleが提供するオープンソースのオペレーティングシステムです。セキュリティ、信頼性、パフォーマンスを重視して設計されています。
*   **セキュリティ修正 (Security Fixes)**: ソフトウェアの脆弱性を修正し、セキュリティリスクを軽減するためのパッチやアップデートです。

---

## Change (Filestore API default enablement)
原文: Starting on June 30, 2026, the Filestore API (`file.googleapis.com`) is enabled by default when you enable the Kubernetes Engine API (`container.googleapis.com`) in a project. The Filestore API is required for PersistentVolumes that use the `ReadWriteMany` access mode in GKE.

説明：
2026年6月30日以降、Google CloudプロジェクトでKubernetes Engine API (`container.googleapis.com`) を有効にする際に、Filestore API (`file.googleapis.com`) がデフォルトで有効になるよう変更されます。このFilestore APIは、GKEで `ReadWriteMany` アクセスモードを使用するPersistentVolumeに必要です。

影響有無：**影響なし**
理由：
*   この変更は将来（2026年6月30日以降）のものであり、現時点では影響ありません。
*   APIがデフォルトで有効になるという変更は、既存のプロジェクトやサービスに悪影響を与えるものではありません。新規プロジェクトでの設定の手間が省けるなどの利便性向上が主な目的です。
*   Google Cloud Composer 2は通常、永続ボリュームにFilestoreを直接使用する構成は一般的ではありません。Airflow DAGsやデータの永続化にはCloud Storageを使用することが一般的です。したがって、Composerの既存の運用に直接的な影響はありません。

対処方法：
現時点では特別な対処は不要です。将来、GKEでFilestoreをPersistentVolumeとして利用する際に、この変更によってAPIの有効化が自動で行われることを認識しておくと良いでしょう。

用語説明：
*   **Filestore API**: Google Cloudが提供する高性能なマネージドファイルストレージサービスであるFilestoreを操作するためのAPIです。
*   **Kubernetes Engine API**: GKEクラスターの作成、管理など、Kubernetes Engineサービスを操作するためのAPIです。
*   **PersistentVolume (PV)**: Kubernetesにおける永続ストレージのリソースです。Podのライフサイクルから独立してデータが保存されます。
*   **`ReadWriteMany` アクセスモード**: 複数のPodやノードから同時に読み書きが可能なPersistentVolumeアクセスモードです。共有ファイルシステムのようなストレージ（例: Filestore）でよく使用されます。

---