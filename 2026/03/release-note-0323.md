
# Title: March 19, 2026 
Link: https://docs.cloud.google.com/release-notes#March_19_2026<br>
Google Cloudのリリースノートを元に、構築済みのサービスへの影響有無を調査し、以下の通りご回答いたします。

---

# Apigee X

## Announcement

**原文:**
On March 19th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
If you set a preferred window for maintenance for your instance, and your instance version is below **1-16-0-apigee-6**, your instance will be updated to **1-16-0-apigee-6** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will not be updated:
- Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
- Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).

For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

**説明:**
本アナウンスは、Apigee X インスタンスのメンテナンスアップデートに関するものです。2026年3月19日より、メンテナンスウィンドウを設定しているApigee X インスタンスのうち、バージョンが `1-16-0-apigee-6` 未満のものが、今後7〜21日以内にこのバージョンへ自動的にアップデートされます。アップグレード予定日に関する通知は、今後2営業日以内に送信されます。
ただし、以下のいずれかの条件に該当するインスタンスは、このアップデートの対象外となります。
*   DNS設定に誤りがあるインスタンス（既知の問題 445936920 に記載）。
*   既に廃止されたApigee Java Libraryを使用しているインスタンス（2025年10月16日付のApigeeリリースノートに記載）。

**影響有無:**
**影響あり:**
Apigee X をご利用しており、インスタンスのバージョンが `1-16-0-apigee-6` 未満で、かつメンテナンスウィンドウを設定している場合、お客様のApigee X インスタンスは自動的にアップデートの対象となります。
これにより、新機能の利用やセキュリティパッチの適用などの恩恵を受けられる一方で、既存のAPIプロキシ、カスタムポリシー、統合、またはカスタムJavaコードとの互換性に影響がないか確認が必要になる可能性があります。特に、廃止されたJava Libraryを利用している場合は、アップデートが行われないため、その対処を検討する必要があります。

**対処方法:**
1.  **インスタンスバージョンの確認:** Apigee X インスタンスの現在のバージョンが `1-16-0-apigee-6` 未満であるかを確認してください。
2.  **通知の確認:** 今後2営業日以内に送信される予定のアップグレード予定日の通知を確認し、関係者と共有してください。
3.  **互換性テストの計画:** アップデートが適用される前に、可能な限りテスト環境にて既存のAPIプロキシ、ポリシー、ターゲットエンドポイント、およびカスタムコード（特にJava Calloutなど）が、新しいバージョン (`1-16-0-apigee-6`) で正常に動作するか互換性テストを計画・実施してください。
4.  **未更新インスタンスの対処:** もし、DNS設定ミスや廃止されたApigee Java Libraryの使用が原因でインスタンスが更新されない場合は、速やかにこれらの問題を解決し、最新バージョンへの更新を可能にすることをご検討ください。廃止されたJava Libraryについては、代替手段への移行計画を立てることを推奨します。

**用語説明:**
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームです。APIの設計、セキュリティ、デプロイ、監視、分析をエンドツーエンドで支援します。
*   **メンテナンスウィンドウ (Maintenance Windows)**: クラウドサービスプロバイダがお客様の環境に対して計画的なメンテナンス作業を実施する際に、お客様が事前に指定できる期間です。これにより、サービス中断のリスクを最小限に抑えることができます。
*   **インスタンスバージョン (Instance Version)**: Apigee X サービスの基盤となるソフトウェアの特定のリリースバージョンを指します。
*   **DNS misconfiguration**: ドメインネームシステム (DNS) の設定が誤っている状態を指します。これにより、サービスへのアクセスや名前解決に問題が生じる可能性があります。
*   **Apigee Java Library**: ApigeeのAPIプロキシ内で、Java Calloutポリシーなどを通じてカスタムロジックを実装するために使用できるJavaライブラリです。

---

# Compute Engine

## Breaking (Changed)

**原文:**
**Changed**: The following operations on the boot disk of a Compute Engine instance that has a service account attached require the `iam.serviceAccounts.actAs` permission on the service account. In the following list, the boot disk of such an instance is referred to as the *source disk*.
*   Creating a standard or archive snapshot of the source disk, including application consistent snapshots
*   Cloning the source disk
*   Creating a machine image of the instance
*   Creating a custom image of the source disk
*   Starting asynchronous replication of the source disk to another region
*   Creating a new disk when you create an instance, if the new disk is created from an instant snapshot of the source disk

If you have already have the Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) role and the Service Account User (v1) (`roles/iam.serviceAccountUser`) role on the project, no action is required.
Otherwise, ask your administrator to grant you the `iam.serviceAccounts.actAs` permission on the service account. For instructions, see [Manage access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources).

**説明:**
本変更は、サービスアカウントがアタッチされたCompute Engineインスタンスのブートディスクに対し、特定の操作（スナップショット作成、ディスククローン、マシンイメージ作成、カスタムイメージ作成、非同期レプリケーション開始、インスタントスナップショットからの新規ディスク作成）を実行する際に、ブートディスクにアタッチされたサービスアカウントに対する `iam.serviceAccounts.actAs` 権限が必須となることを示しています。
もし、操作を実行するプリンシパル（ユーザーやサービスアカウント）が、既にプロジェクトレベルで `Compute Instance Admin (v1)`（`roles/compute.instanceAdmin.v1`）ロールと `Service Account User (v1)`（`roles/iam.serviceAccountUser`）ロールの両方を持っている場合、追加の対応は不要です。それ以外の場合、管理者に`iam.serviceAccounts.actAs` 権限の付与を依頼する必要があります。

**影響有無:**
**影響あり:**
サービスアカウントがアタッチされたCompute Engineインスタンスのブートディスクに対し、上記にリストされた操作（例: スナップショット作成、ディスククローン、マシンイメージ作成など）を、特定のユーザーアカウント、または別のサービスアカウント（例: CI/CDパイプラインや自動化スクリプトを実行するサービスアカウント）が実行しており、そのプリンシパルが、対象のサービスアカウントに対する `iam.serviceAccounts.actAs` 権限を直接的または `roles/iam.serviceAccountUser` ロールを通じて間接的に保持していない場合、これらの操作が失敗するようになります。

**影響なし:**
*   上記のリストに記載された操作を全く行っていない場合。
*   操作を実行するユーザーやサービスアカウントが、既にプロジェクトレベルで `roles/compute.instanceAdmin.v1` ロールと `roles/iam.serviceAccountUser` ロールを付与されている場合。
*   操作を実行するユーザーやサービスアカウントが、対象のサービスアカウントに対して `iam.serviceAccounts.actAs` 権限を直接付与されている場合。
*   サービスアカウントがアタッチされていないCompute Engineインスタンスのブートディスクに対する操作の場合。

**Composer v2 (Composer version 2.7.1, Airflow version 2.7.3) への間接的な影響:**
Google Cloud Composerインスタンスは内部的にCompute EngineのVM上で動作し、サービスアカウントがアタッチされています。Composer自体が提供するバックアップ機能などはGoogle Cloudの管理下で行われるため、直接的な影響は少ないと考えられます。しかし、お客様がComposerの基盤VMに対してカスタムでディスクスナップショットを作成したり、カスタムイメージを作成したりする運用を行っている場合は、影響を受ける可能性があります。

**対処方法:**
1.  **影響範囲の特定:** サービスアカウントがアタッチされたCompute Engineインスタンスのブートディスクに対して、上記リストに記載された操作（スナップショット作成、ディスククローン、イメージ作成など）を実行しているユーザー、サービスアカウント、または自動化プロセスを特定してください。
2.  **IAMポリシーの確認:** 特定されたユーザーまたはサービスアカウントのIAMポリシーを確認し、対象のサービスアカウントに対する `iam.serviceAccounts.actAs` 権限が不足しているか、または `roles/iam.serviceAccountUser` ロールが割り当てられているかを確認してください。
3.  **権限の付与:** 権限が不足している場合、以下のいずれかの方法で適切な権限を付与してください。
    *   **推奨:** 操作を実行するプリンシパル（ユーザー、サービスアカウント）に対して、プロジェクトレベルまたは適切なリソースレベルで `roles/iam.serviceAccountUser` ロールを付与します。このロールには `iam.serviceAccounts.actAs` 権限が含まれています。
    *   または、よりきめ細やかな権限管理が必要な場合は、特定のサービスアカウントに対して直接 `iam.serviceAccounts.actAs` 権限を付与します。
4.  **テストの実施:** 権限付与後、影響を受ける可能性のある操作が正常に実行されることをテストし、影響がないことを確認してください。

**用語説明:**
*   **Compute Engine**: Google Cloudが提供するIaaS（Infrastructure as a Service）であり、仮想マシン（VM）インスタンスをホストするサービスです。
*   **ブートディスク (Boot Disk)**: 仮想マシンインスタンスがオペレーティングシステムを起動するために使用する永続ディスクです。
*   **サービスアカウント (Service Account)**: Google Cloudリソースにアクセスするための特別な種類のGoogleアカウントです。VMインスタンスやアプリケーションなどがGoogle Cloud APIとやり取りする際に使用されます。
*   **`iam.serviceAccounts.actAs` 権限**: 別のサービスアカウントを「代理 (act as)」して操作を実行するためのIAM権限です。この権限を持つことで、指定されたサービスアカウントの権限でAPI呼び出しを行うことができるようになります。
*   **スナップショット (Snapshot)**: 永続ディスクのポイントインタイムコピーであり、データバックアップやディスクの複製、データ復元などに使用されます。
*   **マシンイメージ (Machine Image)**: VMインスタンスのブートディスク、データディスク、インスタンスのメタデータ、ネットワーク構成などをすべて含んだ単一のリソースです。VMのバックアップやテンプレートとして使用できます。
*   **カスタムイメージ (Custom Image)**: ユーザーが作成したオペレーティングシステムやアプリケーションが含まれたディスクイメージです。
*   **非同期レプリケーション (Asynchronous Replication)**: ディスクデータを別のリージョンに非同期で複製するプロセスで、ディザスタリカバリなどの目的で使用されます。
*   **インスタントスナップショット (Instant Snapshot)**: ディスクのポイントインタイムビューをほぼ瞬時に作成する機能で、ディスクのI/Oに影響を与えずに迅速にバックアップを作成できます。
*   **IAM (Identity and Access Management)**: Google Cloudのリソースに対するアクセス権限を管理するサービスです。誰がどのリソースに対してどのような操作を行えるかを定義します。
*   **`roles/compute.instanceAdmin.v1`**: Compute Engineインスタンスの管理権限を付与する事前定義IAMロールです。
*   **`roles/iam.serviceAccountUser`**: サービスアカウントを「代理 (act as)」する権限を含む事前定義IAMロールです。このロールを持つことで、他のサービスアカウントの権限で操作を実行できるようになります。

---